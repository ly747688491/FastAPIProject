import os

import casbin
import casbin_tortoise_adapter
from fastapi import FastAPI

from config.setting import settings
from utils.utils_set import get_current_directory


def register_casbin(app: FastAPI):
    adapter = casbin_tortoise_adapter.TortoiseAdapter()
    rule_path = os.path.join(get_current_directory(), "config", settings.CASBIN_MODEL_NAME)
    e = casbin.Enforcer(rule_path, adapter)
    e.enable_auto_save(True)
    app.state.enforcer = e
