from fastapi import FastAPI

from .casbin import register_casbin
from .cors import register_cors
from .exception import register_exception
from .log import logger_init
from .middleware import RegisterMiddleware
from .mount import register_mount
from .redis import register_redis
from .router import register_router
from .tortoise import register_orm


def registerMiddlewareHandle(server: FastAPI):
    # 添加耗时请求中间件
    server.add_middleware(RegisterMiddleware)
