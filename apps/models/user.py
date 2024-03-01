from tortoise import fields
from tortoise.contrib.pydantic import pydantic_model_creator

from apps.models.base import AbstractBaseModel


class User(AbstractBaseModel):
    auth_user_id = fields.CharField(255, null=False, unique=True)
    username = fields.CharField(100, null=True)
    password = fields.CharField(100, null=True)
    mobile = fields.CharField(100, null=True)
    email = fields.CharField(100, null=True)
    status = fields.IntField(null=True)

    class Meta:
        table = "client_users"
        table_description = "save ik user info"
        ordering = ["-create_time", "id"]

    class PydanticMeta:
        exclude = ["create_time", "update_time", "id"]

    def __str__(self):
        return self.auth_user_id or "UserModel"


User_orm = pydantic_model_creator(User, name="User")
