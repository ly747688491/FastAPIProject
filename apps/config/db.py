# 配置文件：DbConfig
from apps.utils.db import DbConfig

db_config = DbConfig()
db_config.host = '127.0.0.1'
db_config.port = '3306'
db_config.username = 'zlsanalysis'
db_config.password = 'zlsanalysis'
db_config.database = 'zlsanalysis'
db_config.echo = True
