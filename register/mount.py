from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from config.setting import settings


def register_mount(app: FastAPI):
    """ 挂载静态文件 -- https://fastapi.tiangolo.com/zh/tutorial/static-files/ """

    # 第一个参数为url路径参数, 第二参数为静态文件目录的路径, 第三个参数是FastAPI内部使用的名字
    app.mount(f"/{settings.STATIC_DIR}", StaticFiles(directory=settings.STATIC_DIR), name=settings.STATIC_DIR)
