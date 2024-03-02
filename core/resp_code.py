from typing import Union

from fastapi import Response
from fastapi.responses import ORJSONResponse
from loguru import logger
from starlette import status


def resp_200(msg: str = "操作成功", **kwargs) -> Response:
    kwargs |= {'code': 200, 'msg': msg}
    logger.info(kwargs)
    return ORJSONResponse(status_code=status.HTTP_200_OK, content=kwargs)


def resp_404(*, data: str = None, msg: str = "请求出错(404)") -> Response:
    return ORJSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={'code': 404, 'msg': msg, 'data': data})


def resp_422(*, data: str = None, msg: Union[list, dict, str] = "不可处理的实体") -> Response:
    return ORJSONResponse(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                          content={'code': 422, 'msg': msg, 'data': data})


def resp_500(*, msg: Union[list, dict, str] = "服务器错误(500)") -> Response:
    """若依必须返回都是HTTP_200_OK"""
    return ORJSONResponse(headers={'Access-Control-Allow-Origin': '*'},
                          status_code=status.HTTP_200_OK,
                          content={'code': 500, 'msg': msg})
