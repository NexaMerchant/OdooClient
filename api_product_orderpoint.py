import os
from dotenv import load_dotenv
from odoo_api import OdooApi # 假设你的 OdooApi 类在这个文件中

load_dotenv()

# --- 配置参数 ---
# 你可以根据需要修改这些默认的补货规则值
DEFAULT_PRODUCT_MIN_QTY = 0.0
DEFAULT_PRODUCT_MAX_QTY = 0.0
DEFAULT_QTY_MULTIPLE = 0.0
# 如果你想为特定的仓库/位置创建规则，可以在这里指定它们的ID
TARGET_WAREHOUSE_ID = 4 # 例如: SZ (仓库ID) 3 SH (仓库ID)
PURCHASE_ROUTE_NAME = 'Buy'
#TARGET_LOCATION_ID = None # 例如: 8 (WH/Stock)
# --- 配置参数结束 ---

if __name__ == "__main__":
    # 初始化 Odoo API 连接
    odoo = OdooApi(os.getenv('URL'), os.getenv('DB'), os.getenv('USERNAME'), os.getenv('API_KEY'))

    print("成功连接到 Odoo。")

    target_warehouse_id = None
    target_location_id = None
    company_id = None

    # 1. 确定目标仓库和位置
    # 尝试获取第一个活动仓库及其默认库存位置
    # 你可能需要根据你的具体需求调整这部分逻辑
    try:
        warehouses = odoo.search_read(
            'stock.warehouse',
            [('active', '=', True), ('id', '=', TARGET_WAREHOUSE_ID)], # 过滤掉指定的仓库ID
            ['id', 'name', 'lot_stock_id', 'company_id'],
        )
        if warehouses:
            warehouse = warehouses[0]
            target_warehouse_id = warehouse['id']
            target_location_id = warehouse['lot_stock_id'][0] if warehouse['lot_stock_id'] else None # lot_stock_id 是一个 many2one 字段
            company_id = warehouse['company_id'][0] if warehouse['company_id'] else None
            print(f"将为仓库 '{warehouse['name']}' (ID: {target_warehouse_id}) 的默认库存位置 (ID: {target_location_id}) 创建补货规则。")
            if not target_location_id:
                print(f"错误：仓库 '{warehouse['name']}' 没有配置默认库存位置 (lot_stock_id)。请检查仓库配置。")
                exit()
            if not company_id:
                print(f"错误：无法确定仓库 '{warehouse['name']}' 的公司。")
                exit()
        else:
            print("错误：在 Odoo 中没有找到活动的仓库。请至少配置一个活动仓库。")
            exit()
    except Exception as e:
        print(f"获取仓库信息时出错: {e}")
        exit()


    # 2. 获取所有产品 (product.product)
    # 你可以添加 domain 来过滤产品，例如只为特定类型或类别的产品创建
    try:
        products = odoo.search_read(
            'product.product',
            [('type', 'in', ['product', 'consu'])], # 通常为可库存产品和消耗品创建补货规则
            ['id', 'name', 'display_name']
        )
        if not products:
            print("没有找到任何产品。")
            exit()
        print(f"找到 {len(products)} 个产品。")
    except Exception as e:
        print(f"获取产品列表时出错: {e}")
        exit()

    # 3. 为每个产品创建重订货规则
    created_rules_count = 0
    skipped_rules_count = 0

    for product in products:
        product_id = product['id']
        product_name = product['display_name']

        print(f"\n正在处理产品: {product_name} (ID: {product_id})")

        # 检查是否已存在针对此产品和位置的补货规则 (重要！)
        try:
            existing_rules = odoo.search_read(
                'stock.warehouse.orderpoint',
                [
                    ('product_id', '=', product_id),
                    ('location_id', '=', target_location_id),
                    ('warehouse_id', '=', target_warehouse_id), # 确保规则与仓库也匹配
                    ('active', '=', True) # 只检查活动的规则
                ],
                ['id']
            )
            if existing_rules:
                print(f"  产品 {product_name} 在位置 ID {target_location_id} 已存在补货规则 (ID: {existing_rules[0]['id']})。跳过创建。")
                skipped_rules_count += 1
                continue
        except Exception as e:
            print(f"  检查现有补货规则时出错: {e}。将尝试创建。")


        # 准备补货规则的数据
        orderpoint_data = {
            'product_id': product_id,
            'location_id': target_location_id,
            'warehouse_id': target_warehouse_id, # 关联到仓库
            'company_id': company_id, # 关联到公司
            'product_min_qty': DEFAULT_PRODUCT_MIN_QTY,
            'product_max_qty': DEFAULT_PRODUCT_MAX_QTY,
            'qty_multiple': DEFAULT_QTY_MULTIPLE,
            'active': True,
            # 'group_id': False, # 如果需要，可以设置补货组
            # 'trigger': 'auto', # 'auto' 或 'manual'
            'route_id': 8, # 如果需要特定的补货路径 购买
        }

        print(f"  准备创建补货规则: {orderpoint_data}")

        

        try:
            rule_id = odoo.create('stock.warehouse.orderpoint', orderpoint_data)
            print(f"  成功为产品 {product_name} 创建补货规则，新规则 ID: {rule_id}")
            created_rules_count += 1
        except Exception as e:
            print(f"  为产品 {product_name} 创建补货规则失败: {e}")
            # 你可能想在这里记录失败的产品或进行其他错误处理
        #exit(0)
    print(f"\n--- 处理完毕 ---")
    print(f"成功创建 {created_rules_count} 条补货规则。")
    print(f"跳过 {skipped_rules_count} 条已存在的补货规则。")