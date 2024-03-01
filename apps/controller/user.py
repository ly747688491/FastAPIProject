from fastapi import APIRouter

from ..schemas.auth import AuthDataSchema, LoginInputSchema
from ..service.user import UserService
from ..utils.system_utils.custom_route import CustomRoute

router = APIRouter(route_class=CustomRoute)


@router.post('/login', response_model=AuthDataSchema, response_model_exclude_unset=True)
async def login(*, login_input: LoginInputSchema):
    """
    用户登录
    :param login_input: 登录结构
    :return:
    """
    if login_input.type == 'token':
        return UserService().login_by_token(login_input.key)
    elif login_input.type == 'openid':
        return UserService().login_by_openid(login_input.key)
    elif login_input.type == 'code':
        return UserService().login_by_code(login_input.key)
    elif login_input.type == 'password':
        return UserService().login_by_password(login_input.key, login_input.password)
    else:
        return {
            'code': 500,
            'message': '登录错误',
        }
