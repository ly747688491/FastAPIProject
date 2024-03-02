from typing import TypeVar, Generic, Optional, Any, List

from loguru import logger
from pydantic import BaseModel
from pydantic.generics import GenericModel


def result_success(code: int = 200, msg: str = "操作成功", **kwargs) -> dict:
    """返回结果"""
    kwargs |= {'code': code, 'msg': msg}
    logger.debug(kwargs)
    return kwargs


def result_success_no_log(code: int = 200, msg: str = "操作成功", **kwargs) -> dict:
    """返回结果"""
    kwargs |= {'code': code, 'msg': msg}
    return kwargs


SchemasType = TypeVar("SchemasType", bound=BaseModel)


class Result(GenericModel, Generic[SchemasType]):
    """ 普通结果 """
    code: int
    msg: str


class ResultData(GenericModel, Generic[SchemasType]):
    """ 带data的结果 """
    code: int
    msg: str
    data: Optional[Any]


class ResultCaptcha(BaseModel):
    """
    验证码结果
    如果设置为captchaEnabled=false，则返回{"msg":"操作成功","code":200,"captchaEnabled":false}\n
    如果设置为captchaEnabled=true，还需要加入img和uuid
    """
    code: int
    msg: str
    captchaEnabled: bool
    img: Optional[str] = None
    uuid: Optional[str] = None


class ResultLogin(BaseModel):
    """
    登陆结果
    成功返回：{"msg":"操作成功","code":200,"token":""}\n
    失败返回：{"msg":"验证码错误","code":500}或{"msg":"用户不存在/密码错误","code":500}\n
    """
    code: int
    msg: str
    token: Optional[str]


class ResultList(GenericModel, Generic[SchemasType]):
    """ 列表结果验证 """
    code: int
    msg: str
    rows: List[SchemasType] = []
    total: int
