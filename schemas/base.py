from datetime import datetime
from typing import Optional, Dict

import orjson
from pydantic import BaseModel, validator


class BaseSch(BaseModel):
    searchValue: Optional[str] = None  # 搜索值
    createBy: Optional[str] = None  # 创建者
    createTime: Optional[datetime] = None  # 搜索值
    updateBy: Optional[str] = None  # 更新者
    updateTime: Optional[datetime] = None  # 更新时间
    remark: Optional[str] = None  # 备注
    params: Optional[Dict] = None  # 请求参数

    @validator("createTime", "updateTime")
    def format_time(cls, value: datetime) -> str:
        if value:
            return value.strftime('%Y-%m-%d %H:%M:%S')  # 格式化时间

    class Config:
        orm_mode = True
        json_loads = orjson.loads
        json_dumps = orjson.dumps
