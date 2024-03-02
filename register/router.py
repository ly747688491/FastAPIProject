from fastapi import FastAPI

from api import api_router


def register_router(app: FastAPI):
    """ 注册路由 """
    app.include_router(api_router.router)  # 虚拟数据的api
