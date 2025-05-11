import os
from dotenv import load_dotenv
from odoo_api import OdooApi # 假设你的 OdooApi 类在这个文件中
import pandas as pd
import warnings
from openpyxl import styles # 确保 openpyxl 已安装
# ... 其他导入 ...

# 在 pd.read_excel 之前
warnings.filterwarnings('ignore', category=UserWarning, module='openpyxl')


load_dotenv()

# --- 配置参数 ---
SOURCE_ORDER_LINE_MODEL = 'external.order.line' # 包含外部SKU和产品ID的订单行模型
SOURCE_EXTERNAL_SKU_FIELD = '库存SKU'      # 订单行模型中的外部SKU字段名
SOURCE_EXTERNAL_SKU_FIELD_2 = '库存SKU中文名称'      # 订单行模型中的外部SKU字段名
SOURCE_EXTERNAL_SKU_FIELD_3 = '库存SKU英文名称'      # 订单行模型中的外部SKU字段名
SOURCE_PRODUCT_ID_FIELD = 'product_id'          # 订单行模型中的Odoo产品ID字段名 (Many2one to product.product)

TARGET_MAPPING_MODEL = 'external.sku.mapping'   # SKU映射模型名
TARGET_EXTERNAL_SKU_FIELD = 'external_sku'      # SKU映射模型中的外部SKU字段名
TARGET_PRODUCT_ID_FIELD = 'product_id'          # SKU映射模型中的Odoo产品ID字段名

PLATFORM = 'mabangerp' # 平台名称

# 如果你的映射模型需要公司ID，并且它不是通过product_id自动设置或默认设置的，
# 你可能需要在这里指定或从源记录中获取它。
# TARGET_COMPANY_ID_FIELD = 'company_id'
# --- 配置参数结束 ---

def create_mapping(odoo, external_sku, product_id, company_id=None):
    """
    检查 SKU 映射记录是否存在，如果存在则返回 ID，否则创建新的映射记录并返回其 ID。
    """
    # 检查映射记录是否存在
    existing_mapping = odoo.search_read(
        TARGET_MAPPING_MODEL,
        [
            (TARGET_EXTERNAL_SKU_FIELD, '=', external_sku),
            (TARGET_PRODUCT_ID_FIELD, '=', product_id),
        ],
        ['id'],
    )
    if existing_mapping:
        print(f"映射记录已存在: {existing_mapping[0]['id']}")
        return existing_mapping[0]['id']
    
    """
    创建 SKU 映射记录
    """
    new_mapping = {
        TARGET_EXTERNAL_SKU_FIELD: external_sku,
        TARGET_PRODUCT_ID_FIELD: product_id,
        # 如果需要，可以添加其他字段，例如 company_id 等
    }
    if company_id:
        new_mapping['company_id'] = company_id

    mapping_id = odoo.create(
        TARGET_MAPPING_MODEL,
        new_mapping,
    )
    print(f"创建新的映射记录: {mapping_id}")
    return mapping_id

if __name__ == "__main__":
    odoo = OdooApi(os.getenv('URL'), os.getenv('DB'), os.getenv('USERNAME'), os.getenv('API_KEY'))
    print("成功连接到 Odoo。")

    # 读取 xls 目录下面的 xls 文件
    xls_dir = os.path.join(os.path.dirname(__file__), 'xls/'+PLATFORM)
    if not os.path.exists(xls_dir):
        print(f"错误：目录 '{xls_dir}' 不存在。")
        exit()
    xls_files = [f for f in os.listdir(xls_dir) if f.endswith('.xlsx')]
    if not xls_files:
        print("没有找到任何 .xls 文件。")
        exit()
    # for 读取每个文件中的内容处理
    for xls_file in xls_files:
        file_path = os.path.join(xls_dir, xls_file)
        print(f"正在处理文件: {file_path}")
        try:
            df = pd.read_excel(file_path)
            #print(df.columns)
            if SOURCE_EXTERNAL_SKU_FIELD not in df.columns:
                print(f"错误：文件 '{xls_file}' 中缺少必要的列 '{SOURCE_EXTERNAL_SKU_FIELD}'。")
                continue
            # 遍历 DataFrame 的每一行
            for index, row in df.iterrows():
                #print(row)
                external_sku = row[SOURCE_EXTERNAL_SKU_FIELD]
                external_sku_2 = row[SOURCE_EXTERNAL_SKU_FIELD_2]
                external_sku_3 = row[SOURCE_EXTERNAL_SKU_FIELD_3]
                # 你可以在这里添加更多的字段处理逻辑，例如获取公司ID等
                # company_id = row[TARGET_COMPANY_ID_FIELD] if TARGET_COMPANY_ID_FIELD in row else None

                product_id = None
                # 查找产品ID (product.product) 的逻辑
                # 基于 external_sku 或其他字段查找产品ID

                product = odoo.search_read(
                    'product.product',
                    [('default_code', '=', external_sku)],  # 假设你使用 default_code 来查找产品
                    ['id'],
                )
                if product:
                    product_id = product[0]['id']
                else:
                    print(f"未找到产品 (default_code: {external_sku})。")
                    continue
                
                print(f"找到产品 ID: {product_id} (default_code: {external_sku})")
                
                # 创建新的映射记录
                mapping_id = create_mapping(odoo, external_sku, product_id)
                mapping_id = create_mapping(odoo, external_sku_2, product_id)
                mapping_id = create_mapping(odoo, external_sku_3, product_id)
                #exit()
                    
                    
                    

                #exit()

        except Exception as e:
            print(f"处理文件 '{xls_file}' 时出错: {e}")
        finally:
            # 关闭文件或其他清理操作（如果需要）
            pass
    exit()