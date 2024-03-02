from fastapi import FastAPI
from loguru import logger

from config.setting import settings
from core.redis import CustomRedis


async def register_redis(app: FastAPI):
    redis: CustomRedis = await init_redis_pool()  # redis
    app.state.redis = redis


# 参考: https://github.com/grillazz/fastapi-redis/tree/main/app
async def init_redis_pool() -> CustomRedis:
    """ 连接redis """
    result = await CustomRedis.from_url(url=settings.REDIS_URL, encoding=settings.GLOBAL_ENCODING,
                                        decode_responses=True)
    logger.info("初始化redis成功")
    return result
