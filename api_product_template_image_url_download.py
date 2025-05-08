import os
from dotenv import load_dotenv
from odoo_api import OdooApi
from urllib.parse import urlparse
import base64
import requests # Ensure requests is imported at the top
from io import BytesIO # To handle image data in memory
from PIL import Image # For image conversion

load_dotenv()

if __name__ == "__main__":
    # Odoo
    odoo = OdooApi(os.getenv('URL'), os.getenv('DB'), os.getenv('USERNAME'), os.getenv('API_KEY'))
    # Get a product template image url
    search_criteria = [
        ['image_url', '!=', False],
       # ['image_1920', '=', False], # Temporarily remove or adjust if this causes issues with initial search
         ['id', '=', 11335], # Example ID
    ]
    order_by = "id ASC"
    # Request 'image_url' and 'id'. 'image_1920' will be updated.
    product_template_image_urls = odoo.search_read('product.template', search_criteria, ['id', 'image_url'])

    for product_template_image_url in product_template_image_urls:
        print(f"Product Template ID: {product_template_image_url['id']}, Image URL: {product_template_image_url['image_url']}")
        # check the image url is valid
        parsed_url = urlparse(product_template_image_url['image_url'])
        if parsed_url.scheme and parsed_url.netloc:
            file_name_from_url = os.path.basename(parsed_url.path)
            # It's better to use a consistent extension for the target format, e.g., .png
            base_file_name, _ = os.path.splitext(file_name_from_url)
            target_file_name = base_file_name + ".png" # Convert to PNG
            file_path = os.path.join(os.getenv('IMAGE_URL_DOWNLOAD_PATH'), target_file_name)

            image_content_for_odoo = None # This will hold the content of the converted image

            # We always try to download and convert, or load converted if exists
            # This simplifies logic if the source is always webp and we always want png for Odoo

            print(f"Attempting to process image for {product_template_image_url['image_url']}")
            try:
                response = requests.get(product_template_image_url['image_url'], timeout=10)
                response.raise_for_status() # Raise an exception for HTTP errors
                
                original_image_content = response.content
                print(f"Successfully downloaded image from URL.")

                # Convert image to PNG
                try:
                    img = Image.open(BytesIO(original_image_content))
                    # Ensure the image is in a mode that PNG supports well, e.g., RGBA or RGB
                    if img.mode not in ('RGB', 'RGBA'):
                        img = img.convert('RGBA')
                    
                    output_buffer = BytesIO()
                    img.save(output_buffer, format="PNG")
                    image_content_for_odoo = output_buffer.getvalue()
                    print(f"Image successfully converted to PNG format.")

                    # Optionally save the converted PNG locally
                    # Ensure IMAGE_URL_DOWNLOAD_PATH directory exists
                    download_path_dir = os.getenv('IMAGE_URL_DOWNLOAD_PATH')
                    if not os.path.exists(download_path_dir):
                        os.makedirs(download_path_dir)
                    with open(file_path, 'wb') as f:
                        f.write(image_content_for_odoo)
                    print(f"Converted PNG image saved to {file_path}")

                except Exception as e:
                    print(f"Error converting image {product_template_image_url['image_url']} to PNG: {e}")
                    continue # Skip to next product if conversion fails

            except requests.exceptions.RequestException as e:
                print(f"Error downloading {product_template_image_url['image_url']}: {e}")
                continue # Skip to next product if download fails
            except Exception as e:
                print(f"An unexpected error occurred during download/processing for {product_template_image_url['image_url']}: {e}")
                continue


            if image_content_for_odoo:
                # update the product template image_1920 field
                image_1920_bytes = base64.b64encode(image_content_for_odoo)
                image_1920_string = image_1920_bytes.decode('utf-8')
                try:
                    odoo.write('product.template', [product_template_image_url['id']], {'image_1920': image_1920_string})
                    print(f"Successfully updated image_1920 for product ID {product_template_image_url['id']}")
                except Exception as e:
                    print(f"Error writing image to Odoo for product ID {product_template_image_url['id']}: {e}")
            else:
                print(f"Skipping Odoo update for product ID {product_template_image_url['id']} due to missing image content.")
        #exit(0) # If you want to test with one item