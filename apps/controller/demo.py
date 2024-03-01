from fastapi import APIRouter, Depends

from ..schemas.base import RespListSchema, ListArgsSchema, RespIdSchema, RespBaseSchema
from ..schemas.demo import DemoRespDetailSchema, DemoInfoSchema
from ..service.demo import DemoService
from ..utils.system_utils.auth import get_auth_data
from ..utils.system_utils.custom_route import CustomRoute

router = APIRouter(route_class=CustomRoute)


@router.post('/list', response_model=RespListSchema)
async def list(*, args: ListArgsSchema, auth_data: dict = Depends(get_auth_data)):
    args.user_id = auth_data.get('user_id')
    return DemoService(auth_data).list(args)


@router.get('/{id}', response_model=DemoRespDetailSchema)
async def read(id: int, auth_data: dict = Depends(get_auth_data)):
    resp = DemoRespDetailSchema()
    resp.detail = DemoService(auth_data).read(id)
    return resp


@router.post('', response_model=RespIdSchema, response_model_exclude_none=True)
async def create(*, info: DemoInfoSchema, auth_data: dict = Depends(get_auth_data)):
    return DemoService(auth_data).create(info)


@router.put('/{id}', response_model=RespBaseSchema)
async def update(*, info: DemoInfoSchema, auth_data: dict = Depends(get_auth_data)):
    return DemoService(auth_data).update(info)


@router.delete('/{id}', response_model=RespBaseSchema)
async def delete(id: int, auth_data: dict = Depends(get_auth_data)):
    return DemoService(auth_data).delete(id)
