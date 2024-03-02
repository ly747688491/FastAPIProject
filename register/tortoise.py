from types import ModuleType
from typing import Dict, Iterable, Optional, Union

from fastapi import FastAPI
from tortoise import Tortoise, connections
from tortoise.log import logger

from config.setting import settings


async def register_orm(app: FastAPI):
    await init_orm(db_url=settings.DB_URL,  # 数据库信息
                   modules={"models": settings.DB_MODELS},  # models列表
                   generate_schemas=False,  # 如果数据库为空，则自动生成对应表单,生产环境不要开)
                   )


async def init_orm(config: Optional[dict] = None,
                   config_file: Optional[str] = None,
                   db_url: Optional[str] = None,
                   modules: Optional[Dict[str, Iterable[Union[str, ModuleType]]]] = None,
                   generate_schemas: bool = False,
                   ) -> None:  # pylint: disable=W0612
    await Tortoise.init(config=config, config_file=config_file, db_url=db_url, modules=modules)
    logger.info("Tortoise-ORM 初始化成功, %s, %s", connections._get_storage(), Tortoise.apps)
    if generate_schemas:
        logger.info("Tortoise-ORM generating schema")
        await Tortoise.generate_schemas()


async def close_orm() -> None:  # pylint: disable=W0612
    await connections.close_all()
    logger.info("Tortoise-ORM shutdown")


TORTOISE_ORM = {
    "connections": {"default": settings.DB_URL},
    "apps": {
        "models": {
            "models": ["aerich.models"] + settings.DB_MODELS,
            # 须添加“aerich.models” 后者“models”是上述models.py文件的路径
            "default_connection": "default",
        },
    },
}
