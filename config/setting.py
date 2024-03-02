import secrets
from functools import lru_cache
from typing import Optional

from pydantic import BaseSettings

project_desc = """
    🎉 管理员信息 🎉
    ✨ 账号: admin ✨
    ✨ 密码: admin123 ✨
"""


class Settings(BaseSettings):
    DEBUG: bool = True  # 开发模式配置
    TITLE: str = "FastAPI"  # 项目文档
    DESCRIPTION: str = project_desc  # 描述
    VERSION: str = "v1.0"  # 版本

    # Uvicorn
    UVICORN_HOST: str = '127.0.0.1'
    UVICORN_PORT: int = 8001
    UVICORN_RELOAD: bool = True

    API_PREFIX: str = "/dev-api"  # 接口前缀
    DOCS_URL: str = "/dev-api/docs"  # 文档地址 默认为docs
    REDOC_URL: Optional[str] = "/dev-api/redoc"  # redoc 文档
    OPENAPI_URL: str = "/dev-api/openapi.json"  # 文档关联请求数据接口
    STATIC_DIR: str = 'static'  # 静态文件目录
    GLOBAL_ENCODING: str = 'utf-8'  # 全局编码
    # 跨域请求
    # CORS_ORIGINS: List[AnyHttpUrl] = ["*", "http://127.0.0.1:8001"]

    # Token
    # 密钥(每次重启服务密钥都会改变, token解密失败导致过期, 可设置为常量)
    SECRET_KEY: str = secrets.token_urlsafe(32)
    # SECRET_KEY: str = '1VkVF75nsNABBjK_7-qz7GtzNy3AMvktc9TCPwKczCk'
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 3  # token过期时间: 60 m * 3 hour
    ALGORITHM: str = "HS512"  # 生成token的加密算法

    ADMIN_USERNAME = "admin"
    ADMIN_PASSWORD = "admin123"

    # loguru
    LOGGER_DIR: str = "logs"  # 日志文件夹名
    LOGGER_NAME: str = '{time:YYYY-MM-DD_HH-mm-ss}.log'  # 日志文件名 (时间格式)
    LOGGER_LEVEL: str = 'DEBUG'  # 日志等级: ['DEBUG' | 'INFO']
    LOGGER_ROTATION: str = "12:00"  # 日志分片: 按 时间段/文件大小 切分日志. 例如 ["500 MB" | "12:00" | "1 week"]
    LOGGER_RETENTION: str = "7 days"  # 日志保留的时间: 超出将删除最早的日志. 例如 ["1 days"]

    # Database
    DB_ECHO: bool = False  # 是否打印数据库日志 (可看到创建表、表数据增删改查的信息)
    DB_HOST: str = '127.0.0.1'
    DB_PORT: int = 3306
    DB_USER: str = 'caiqian'
    DB_PASSWORD: str = 'Liy_0123'
    DB_DATABASE: str = 'test_temp'
    DB_CHARSET: str = 'utf8mb4'
    DB_URL = f"mysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}?charset=utf8mb4"
    DB_MODELS = ["models.oper_log", "models.job_info"]

    # Redis
    REDIS_HOST: str = '127.0.0.1'
    REDIS_PORT: int = 6379
    REDIS_PASSWORD: str = 'Liy_0123'
    REDIS_DATABASE: int = 4
    REDIS_TIMEOUT: int = 10
    REDIS_URL: str = f"redis://:{REDIS_PASSWORD}@{REDIS_HOST}:{REDIS_PORT}/{REDIS_DATABASE}?encoding=utf-8"

    # Casbin
    CASBIN_MODEL_NAME: str = 'rbac_model.conf'

    class Config:
        case_sensitive = True  # 区分大小写


@lru_cache
def get_settings():
    """ 读取配置优化写法 """
    return Settings()


settings = Settings()
