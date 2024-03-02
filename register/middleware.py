import time

from fastapi import Request
from loguru import logger
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response

from service.oper_log import OperLogService


class RegisterMiddleware(BaseHTTPMiddleware):
    def __init__(self, app):
        super.__init__(app)

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
