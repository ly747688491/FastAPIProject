import traceback


from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import ORJSONResponse
from loguru import logger

from pydantic import ValidationError
from starlette.exceptions import HTTPException
from starlette.status import HTTP_401_UNAUTHORIZED

from core.cust_exc import LoginException, AccessTokenFail, CommonException, PermissionNotEnough
from core.resp_code import resp_500, resp_422


def register_exception(app: FastAPI):
    """ 全局异常捕获 -- https://www.charmcode.cn/article/2020-07-19_fastapi_exception """

    # -----------------------------------------全局异常------------------------------------------------- #
    @app.exception_handler(Exception)
    async def all_exception_handler(request: Request, exc: Exception):
        """ 捕获全局异常 """
        logger.error(
            f"全局异常\n{request.method}URL:{request.url}\nHeaders:{request.headers}\n{traceback.format_exc()}")
        return resp_500(msg="服务器内部错误")

    # -----------------------------------------FastAPI异常------------------------------------------------- #
    @app.exception_handler(RequestValidationError)
    async def request_validation_exception_handler(request: Request, exc: RequestValidationError):
        """ 请求参数验证异常 """
        logger.error(
            f"请求参数格式错误\nURL:{request.method}-{request.url}\nHeaders:{request.headers}\nerror:{exc.errors()}")
        return resp_422(msg=exc.errors())

    @app.exception_handler(HTTPException)
    async def error_http_handler(request: Request, exc: HTTPException):
        """ 重写HTTPException异常 """
        logger.warning(f"{exc.detail}\nURL:{request.method}-{request.url}\nHeaders:{request.headers}")
        msg = "服务器内部错误"
        if exc.status_code == HTTP_401_UNAUTHORIZED:
            msg = "认证失败，无法访问系统资源."
        return ORJSONResponse(status_code=exc.status_code,
                              content={'code': exc.status_code, 'msg': msg, 'data': exc.detail})

    # -----------------------------------------pydantic异常------------------------------------------------- #
    @app.exception_handler(ValidationError)
    async def inner_validation_exception_handler(request: Request, exc: ValidationError):
        """ 内部参数验证异常 """
        logger.error(
            f"内部参数验证错误\nURL:{request.method}-{request.url}\nHeaders:{request.headers}\nerror:{exc.errors()}")
        return resp_500(msg=exc.errors())

    # -------------------------------自定义异常------------------------------------------------- #
    @app.exception_handler(LoginException)
    async def login_exception_handler(request: Request, exc: LoginException):
        """ 登录异常(自定义异常) """
        logger.warning(f"{exc.err_desc}\nURL:{request.method}-{request.url}\nHeaders:{request.headers}")
        return resp_500(msg=exc.err_desc)

    @app.exception_handler(AccessTokenFail)
    async def access_token_fail_handler(request: Request, exc: AccessTokenFail):
        """ 登录异常(自定义异常) """
        logger.warning(f"{exc.err_desc}\nURL:{request.method}-{request.url}\nHeaders:{request.headers}")
        return resp_500(msg=exc.err_desc)

    @app.exception_handler(CommonException)
    async def common_except_handler(request: Request, exc: CommonException):
        """ 登录异常(自定义异常) """
        logger.warning(f"{exc.err_desc}\nURL:{request.method}-{request.url}\nHeaders:{request.headers}")
        return resp_500(msg=exc.err_desc)

    @app.exception_handler(PermissionNotEnough)
    async def permission_not_enough_handler(request: Request, exc: PermissionNotEnough):
        """ 登录异常(自定义异常) """
        logger.warning(f"{exc.err_desc}\nURL:{request.method}-{request.url}\nHeaders:{request.headers}")
        return resp_500(msg=exc.err_desc)
