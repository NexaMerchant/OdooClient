from enum import Enum

class RedisEnums(Enum):
    PRODUCT = "product"
    ATTRIBUTE = "attribute"
    ATTRIBUTE_VALUE = "attribute_value"
    CATEGORY = "category"
    USER = "user"
    SESSION = "session"

class RedisProductEnums(Enum):
    PRODUCT_ID = "product_id"
    PRODUCT_NAME = "product_name"
    PRODUCT_DESCRIPTION = "product_description"
    PRODUCT_PRICE = "product_price"
    PRODUCT_CATEGORY = "product_category"
    PRODUCT_ATTRIBUTES = "product_attributes"

class RedisAttributeEnums(Enum):
    ATTRIBUTE_ID = "attribute_id"
    ATTRIBUTE_NAME = "attribute_name"
    ATTRIBUTE_DESCRIPTION = "attribute_description"
    ATTRIBUTE_TYPE = "attribute_type"
    ATTRIBUTE_VALUES = "attribute_values"

class RedisAttributeValueEnums(Enum):
    ATTRIBUTE_VALUE_ID = "attribute_value_id"
    ATTRIBUTE_VALUE_NAME = "attribute_value_name"
    ATTRIBUTE_VALUE_DESCRIPTION = "attribute_value_description"

class RedisCategoryEnums(Enum):
    CATEGORY_ID = "category_id"
    CATEGORY_NAME = "category_name"
    CATEGORY_DESCRIPTION = "category_description"
    CATEGORY_PARENT = "category_parent"

class RedisUserEnums(Enum):
    USER_ID = "user_id"
    USER_NAME = "user_name"
    USER_EMAIL = "user_email"
    USER_PASSWORD = "user_password"
    USER_ROLE = "user_role"

class RedisSessionEnums(Enum):
    SESSION_ID = "session_id"
    SESSION_USER_ID = "session_user_id"
    SESSION_START_TIME = "session_start_time"
    SESSION_END_TIME = "session_end_time"
