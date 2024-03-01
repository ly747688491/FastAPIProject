import json

from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from starlette.middleware.cors import CORSMiddleware
from starlette.requests import Request
from starlette.responses import Response
from starlette.staticfiles import StaticFiles

from apps.config.anonymous import anonymous_path_list
from apps.config.database import db_init

from apps.config.fastapi import FastapiConfig
from apps.config.redis import redis_config
from apps.controller.api_v1 import api_v1_router
from apps.controller.base import base_router
from apps.utils.system_utils.auth import get_auth_data_by_authorization
from apps.utils.system_utils.redis import RedisUtils
from apps.utils.system_utils.request_log import update_log, create_log

RedisUtils.default_config = redis_config

app = FastAPI(**FastapiConfig.__dict__)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    await update_log(request.state.log, Response(json.dumps({
        'code': 400,
        'message': 'Request Validation Error',
        'error_detail': str(exc),
    }), status_code=400))

    return Response(json.dumps({
        'code': 400,
        'message': 'Request Validation Error',
    }), status_code=400)


@app.exception_handler(Exception)
async def http_exception_handler(request, exc):
    await update_log(request.state.log, Response(json.dumps({
        'code': 500,
        'message': 'Internal Server Error',
        'error_detail': str(exc),
    }), status_code=500))

    return Response(json.dumps({
        'code': 500,
        'message': 'Internal Server Error',
    }), status_code=500)


@app.middleware('http')
async def auth_token(req: Request, call_next):
    response_type = 1
    response = Response(json.dumps({
        'code': 401,
        'message': 'Unauthorized',
    }), status_code=401)
    path = req.method + req.url.path

    # 判断是否可匿名访问
    if path in anonymous_path_list or path.find('GET/res/') == 0:
        response_type = 2
        response = await call_next(req)
    elif auth_data := get_auth_data_by_authorization(
        req.headers.get('authorization'), 360000
    ):
        response_type = 3
        response = await call_next(req)

    if response_type == 1:
        log = await create_log(req)
        await update_log(log, response)

    return response


app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(base_router)
app.include_router(api_v1_router, prefix='/v1')
app.mount('/res', StaticFiles(directory=FastapiConfig.res_path), name='res')

db_init(app)
