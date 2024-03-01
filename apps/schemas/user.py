from pydantic import BaseModel

from apps.models.user import User_orm


class UserStatus(BaseModel):
    status: str
    name: str


class UserInfo(User_orm):
    pass
