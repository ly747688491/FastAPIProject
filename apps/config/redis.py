from apps.utils.system_utils.redis import RedisConfig
from config import configs

redis_config = RedisConfig()
redis_config.host = configs.REDIS_HOST
redis_config.port = configs.REDIS_PORT
redis_config.password = configs.REDIS_PASSWORD
redis_config.database = configs.REDIS_DB
