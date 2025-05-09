import os
import base64
import requests
from dotenv import load_dotenv
from urllib.parse import urlparse
from odoo_api import OdooApi # 假设你的 OdooApi 类在这个文件中

load_dotenv()

# --- 配置 ---
MODEL_NAME = 'external.order.line'
TEXT_IMAGE_FIELD = 'images' # 包含 URL 或 Base64 字符串的文本字段
BINARY_IMAGE_FIELD = 'images_binary' # 目标二进制字段
# --- 配置结束 ---

def is_valid_url(url_string):
    """检查字符串是否是有效的 HTTP/HTTPS URL"""
    if not isinstance(url_string, str):
        return False
    try:
        result = urlparse(url_string)
        return all([result.scheme in ['http', 'https'], result.netloc])
    except ValueError:
        return False

def is_valid_base64(s):
    """检查字符串是否是有效的 Base64"""
    if not isinstance(s, str):
        return False
    try:
        # Python的base64模块在解码非base64字符串时会抛出binascii.Error
        base64.b64decode(s.encode('utf-8'), validate=True)
        return True
    except Exception:
        return False

if __name__ == "__main__":
    odoo = OdooApi(os.getenv('URL'), os.getenv('DB'), os.getenv('USERNAME'), os.getenv('API_KEY'))
    print("成功连接到 Odoo。")

    # 1. 搜索需要处理的记录
    # 我们查找 'images' 字段不为空的记录
    # 你可以根据需要添加更多过滤条件，例如 ('images_binary', '=', False) 来只处理尚未同步的
    domain = [(TEXT_IMAGE_FIELD, '!=', False),
              ('images_binary', '=', False),
              #('external_sku', 'like', "H"), # 仅处理有外部订单ID的记录
              ]
    fields_to_read = ['id', TEXT_IMAGE_FIELD]
    
    print(f"正在从模型 '{MODEL_NAME}' 中搜索记录，条件: {domain}, 读取字段: {fields_to_read}")

    try:
        order_by = 'id desc' # 按 ID 降序排列
        limit = 1000 # 限制每次读取的记录数
        records = odoo.search_read(MODEL_NAME, domain, fields_to_read, order_by=order_by, limit=limit)
    except Exception as e:
        print(f"搜索记录时出错: {e}")
        exit()

    if not records:
        print("没有找到需要处理的记录。")
        exit()

    print(f"找到 {len(records)} 条记录需要处理。")

    processed_count = 0
    updated_count = 0
    error_count = 0

    # 2. 遍历记录并处理
    for record in records:
        record_id = record['id']
        image_data_from_text_field = record.get(TEXT_IMAGE_FIELD)
        base64_to_write = None

        print(f"\n正在处理记录 ID: {record_id}...")

        if not image_data_from_text_field or not isinstance(image_data_from_text_field, str):
            print(f"  记录 ID {record_id}: '{TEXT_IMAGE_FIELD}' 字段为空或非字符串。跳过。")
            error_count +=1
            continue

        # 尝试判断是 URL 还是 Base64
        if is_valid_url(image_data_from_text_field):
            print(f"  记录 ID {record_id}: '{TEXT_IMAGE_FIELD}' 内容识别为 URL: {image_data_from_text_field}")
            try:
                response = requests.get(image_data_from_text_field, timeout=20) # 增加超时时间
                response.raise_for_status() # 如果请求失败则抛出 HTTPError
                image_bytes = response.content
                base64_to_write = base64.b64encode(image_bytes).decode('utf-8')
                print(f"  记录 ID {record_id}: 图片已从 URL 下载并转换为 Base64。")
            except requests.exceptions.RequestException as e_req:
                print(f"  记录 ID {record_id}: 下载 URL '{image_data_from_text_field}' 失败: {e_req}")
                error_count += 1
                continue
            except Exception as e_conv:
                print(f"  记录 ID {record_id}: 处理下载的图片内容时出错: {e_conv}")
                error_count += 1
                continue
        else:
            print(f"  记录 ID {record_id}: '{TEXT_IMAGE_FIELD}' 内容不识别为 URL，尝试作为 Base64 处理。")
            if is_valid_base64(image_data_from_text_field):
                base64_to_write = image_data_from_text_field
                print(f"  记录 ID {record_id}: '{TEXT_IMAGE_FIELD}' 内容确认为有效的 Base64 字符串。")
            else:
                print(f"  记录 ID {record_id}: '{TEXT_IMAGE_FIELD}' 内容既不是有效 URL 也不是有效 Base64 字符串。跳过。")
                error_count += 1
                continue
        
        # 3. 更新 Odoo 中的 'images_binary' 字段
        if base64_to_write:
            try:
                update_data = {BINARY_IMAGE_FIELD: base64_to_write}
                odoo.write(MODEL_NAME, [record_id], update_data)
                print(f"  记录 ID {record_id}: 成功更新 '{BINARY_IMAGE_FIELD}' 字段。")
                updated_count += 1
            except Exception as e_write:
                print(f"  记录 ID {record_id}: 更新 Odoo 记录失败: {e_write}")
                error_count += 1
        else:
            # 此情况理论上应该被前面的 continue 覆盖，但作为安全措施保留
            print(f"  记录 ID {record_id}: 没有可写入的 Base64 数据。跳过更新。")
            
        processed_count += 1

    print(f"\n--- 处理完毕 ---")
    print(f"总共检查记录: {len(records)}")
    print(f"成功处理并尝试更新的记录: {processed_count}")
    print(f"成功更新到 Odoo 的记录: {updated_count}")
    print(f"发生错误的记录 (跳过): {error_count}")