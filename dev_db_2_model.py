import os



from apps.config.database import db_config
from apps.utils.system_utils.sync_model import SyncModel

# 同步Model：根据数据库中的表结构。

if __name__ == '__main__':
    app_dir = os.path.dirname(os.path.abspath(__file__)) + os.sep + 'app'
    SyncModel().sync(app_dir, db_config, is_use_base_model=True)