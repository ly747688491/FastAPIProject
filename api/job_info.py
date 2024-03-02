import pandas as pd
from fastapi import APIRouter
from tortoise.contrib.pydantic import pydantic_queryset_creator

from core.result import ResultData
from models.job_info import JobInfoDb

router = APIRouter(prefix="/job", tags=["岗位数据"])


@router.get("/jobs_by_city", response_model=ResultData, summary='获取redis信息')
async def get_jobs_by_city():
    Job_Pydantic = pydantic_queryset_creator(JobInfoDb)
    jobs = await Job_Pydantic.from_queryset(JobInfoDb.all())
    df = pd.DataFrame([dict(job) for job in jobs])

    return df['city'].value_counts().to_dict()
