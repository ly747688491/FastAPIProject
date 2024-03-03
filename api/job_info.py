from fastapi import APIRouter

from core.result import ResultData

router = APIRouter(prefix="/job", tags=["岗位数据"])


@router.get("/jobs_by_city", response_model=ResultData, summary='获取redis信息')
async def get_jobs_by_city():
    pass
