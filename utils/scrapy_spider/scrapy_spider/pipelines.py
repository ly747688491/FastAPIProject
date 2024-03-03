import os
import time

from tortoise import Tortoise
from tortoise.transactions import in_transaction
from twisted.internet import defer

from config import settings
from models.job_info import JobInfoDb


class ScrapySpiderPipeline:

    @defer.inlineCallbacks
    async def open_spider(self, spider):
        await Tortoise.init(db_url=settings.DB_URL, modules={"models": settings.DB_MODELS})
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        print('开始爬取')

    async def process_item(self, item, spider):
        async with in_transaction("default") as conn:
            job = JobInfoDb()
            job.position_name = item['job_name']
            job.salary_range = item['job_salary']
            job.location = item['job_city']
            job.work_experience = item['job_experience']
            job.education_requirement = item['job_education']
            job.position_tag = item['job_tags']
            job.company_name = item['company_name']
            job.company_type = item['company_type']
            job.company_size = item['company_size']
            await conn.save(job)
        return item

    def close_spider(self, spider):
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        print('爬取结束')
