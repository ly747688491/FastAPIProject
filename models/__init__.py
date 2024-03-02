from tortoise import fields
from tortoise.models import Model


class BaseTimeModel(Model):
    createBy = fields.CharField(source_field="create_by", max_length=64, null=True, default="", describe="创建者")
    createTime = fields.DatetimeField(source_field="create_time", auto_now_add=True, null=True, describe="创建时间")
    updateBy = fields.CharField(source_field="update_by", max_length=64, null=True, default="", describe="更新者")
    updateTime = fields.DatetimeField(source_field="update_time", auto_now=True, null=True, describe="更新时间")

    def to_dict(self):  # 这个方法自定义的时候使用
        return {i: getattr(self, i) for i in self.__dict__ if not i.startswith('_')}

    class Meta:
        abstract = True
