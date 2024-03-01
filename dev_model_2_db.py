from sqlalchemy import create_engine

from apps.config.database import db_config
from apps.models.base import Base

# 根据Mode创建DB数据表

if __name__ == '__main__':
    # 创建db连接
    engine = create_engine(db_config.get_url(), echo=True)

    # 创建db表
    Base.metadata.create_all(engine)
