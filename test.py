import xmlrpc.client
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Odoo server details
url = os.getenv('URL')
db = os.getenv('DB')
username = os.getenv('USERNAME')
api_key = os.getenv('API_KEY')

# Common endpoint
common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))

# Authenticate using API key
uid = common.authenticate(db, username, api_key, {})

print("User ID:", uid)


# Object endpoint
models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

# Function to search for records
def search_records(model, domain):
    return models.execute_kw(db, uid, api_key, model, 'search', [domain])

# Function to create a new record
def create_record(model, values):
    return models.execute_kw(db, uid, api_key, model, 'create', [values])

# Example usage
if __name__ == "__main__":
    # Search for partners with name 'John Doe'
    domain = [('email', '=', 'jane.doe@example.com')]
    partner_ids = search_records('res.partner', domain)
    print("Partner IDs:", partner_ids)

    # Create a new partner
    # new_partner = {
    #     'name': 'Jane Doe',
    #     'email': 'jane.doe@example.com',
    # }
    # partner_id = create_record('res.partner', new_partner)
    # print("New Partner ID:", partner_id)