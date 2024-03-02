from fastapi import APIRouter

from config.setting import settings
from core.result import Result

router = APIRouter(prefix=settings.API_PREFIX)


@router.get("/", response_model=Result, summary='访问首页，提示语')
async def get_index():
    return "欢迎使用。"
