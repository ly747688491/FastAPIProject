from aioredis import Redis
from loguru import logger


def get_login_tokens_key(uuid: str) -> str:
    """# 登录用户 redis key"""
    return f"login_tokens:{uuid}"


def get_config_key(configKey: str) -> str:
    """# 参数管理 cache key"""
    return f"sys_config:{configKey}"


def get_dict_type_key(dictType: str) -> str:
    """# 参数管理 cache key"""
    return f"sys_dict:{dictType}"


def get_captcha_codes_key(uuid: str) -> str:
    """# 参数管理 cache key"""
    return f"captcha_codes:{uuid}"


class CustomRedis(Redis):
    """ 继承Redis,并添加自己的方法 """

    def get_cmdstat_list(self, cmdstat_dict):
        cmdstat_list = []
        for key, value in cmdstat_dict.items():
            name = key.split("_")[-1]
            val = str(value["calls"])
            cmdstat_list.append({"name": name, "value": val})
        return cmdstat_list

    async def loading_config_cache(self):
        """载入config到redis"""
        # 从数据库读取sys_config
        configs = await SysConfigDao.get_list_db()
        # 循环写入redis
        for config in configs:
            await self.set(get_config_key(config.configKey), config.configValue)
        logger.debug("redis存储sys_config成功。")
