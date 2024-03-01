from sqlalchemy.ext.declarative import declarative_base
from tortoise import Model, fields

DeclarativeBase = declarative_base()


class AbstractBaseModel(Model):
    id = fields.IntField(pk=True)
    create_time = fields.DatetimeField(null=True, auto_now_add=True)
    update_time = fields.DatetimeField(null=True, auto_now=True)
    is_delete = fields.IntField(null=False, default="0")

    class Meta:
        abstract = True
