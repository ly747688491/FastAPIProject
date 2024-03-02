import time
from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI, Request
from loguru import logger
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import FileResponse, Response

from config.setting import settings
from register import register_redis, register_orm, register_router, \
    register_exception, register_mount, logger_init
from service.oper_log import OperLogService


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("startup")  # 初始化日志
    await create_app()  # 加载注册中心
    yield
    logger.info("shutdown")


app = FastAPI(description=settings.DESCRIPTION, version=settings.VERSION, debug=settings.DEBUG,
              title=settings.TITLE, docs_url=settings.DOCS_URL, openapi_url=settings.OPENAPI_URL,
              redoc_url=settings.REDOC_URL, lifespan=lifespan)


@app.middleware('http')
async def logger_request(self, request: Request, call_next) -> Response:
    """
    请注意，这样的实现在响应流的主体不适合你的服务器内存时是有问题的（想象一下100GB的响应）。根据你的应用程序的作用，你将裁定这是否是一个问题。
    """
    # 返回性能计数器的值（以分秒为单位）
    start_time = time.perf_counter()
    response = await call_next(request)
    end_time = time.perf_counter()
    logger.debug(
        f"{response.status_code} {request.client.host} {request.method} {request.url} {end_time - start_time}s")
    return await OperLogService(request, response).log_oper()


app.add_middleware(
    CORSMiddleware,
    # allow_origins=[str(origin) for origin in settings.CORS_ORIGINS], # 允许访问的源
    allow_origins=["*"],  # 允许访问的源
    allow_credentials=True,  # 支持 cookie
    allow_methods=("GET", "POST", "PUT", "DELETE"),  # 允许使用的请求方法
    allow_headers=("*", "authentication"),  # 允许携带的 Headers
)


async def create_app():
    """ 注册中心 """
    logger_init()  # 日志初始化

    register_mount(app)  # 挂载静态文件

    register_exception(app)  # 注册捕获全局异常

    register_router(app)  # 注册路由

    await register_orm(app)  # 注册数据库

    await register_redis(app)  # 注册redis

    logger.info("startup over")  # 初始化日志


@app.get("/")
async def root():
    return "Welcome To FastAPI."


@app.get('/favicon.ico', include_in_schema=False)
def favicon():
    return FileResponse('favicon.ico')


if __name__ == '__main__':
    """
    app	运行的 py 文件:FastAPI 实例对象
    host	访问url，默认 127.0.0.1
    port	访问端口，默认 8080
    reload	热更新，有内容修改自动重启服务器
    debug	同 reload
    reload_dirs	设置需要 reload 的目录，List[str] 类型
    log_level	设置日志级别，默认 info
    """
    uvicorn.run(app='main:app', host=settings.UVICORN_HOST, port=settings.UVICORN_PORT, reload=settings.UVICORN_RELOAD)
