from fastapi import APIRouter

from config.setting import settings
from core.result import Result
from . import job_info

router = APIRouter(prefix=settings.API_PREFIX)
router.include_router(job_info.router)


@router.get("/", response_model=Result, summary='访问首页，提示语')
async def get_index():
    return "欢迎使用。"
