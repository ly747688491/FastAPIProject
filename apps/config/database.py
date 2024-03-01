import redis
from tortoise.contrib.fastapi import register_tortoise


from config import configs

SQLALCHEMY_DATABASE_URL = f"mysql://{configs.MYSQL_USER}:{configs.MYSQL_PASSWORD}@{configs.MYSQL_SERVER}:{configs.MYSQL_PORT}/{configs.MYSQL_DB_NAME}?charset=utf8"

# 数据库迁移配置
TORTOISE_ORM = {
    "connections": {"default": SQLALCHEMY_DATABASE_URL},
    "apps": {
        "models": {
            "models": ["aerich.models", "app.models.model"],
            # 须添加“aerich.models” 后者“models”是上述models.py文件的路径
            "default_connection": "default",
        },
    },
}


def db_init(app):
    register_tortoise(
        app,
        db_url=SQLALCHEMY_DATABASE_URL,
        modules={"models": ["app.models.model"]},
        generate_schemas=True,
        add_exception_handlers=True,
    )
