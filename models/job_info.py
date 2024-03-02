from tortoise import fields
from tortoise.models import Model


class JobInfoDb(Model):
    id = fields.IntField(pk=True)
    position_name = fields.CharField(max_length=100)
    salary_range = fields.CharField(max_length=100)
    location = fields.CharField(max_length=100)
    work_experience = fields.CharField(max_length=100)
    education_requirement = fields.CharField(max_length=100)
    position_tag = fields.CharField(max_length=100)
    company_name = fields.CharField(max_length=100)
    company_type = fields.CharField(max_length=100)
    company_size = fields.CharField(max_length=100)
    province = fields.CharField(max_length=100)
    city = fields.CharField(max_length=100)

    class Meta:
        table = "job_info"
        table_description = "岗位信息表"
