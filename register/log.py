import logging
import os

from loguru import logger

from config.setting import settings
from utils.utils_set import create_dir


# 创建日志文件名
def logger_file() -> str:
    """ 创建日志文件名 """
    log_path = create_dir(settings.LOGGER_DIR)
    # 日志输出路径
    return os.path.join(log_path, settings.LOGGER_NAME)


# 将已写好的logging集成到loguru中
class InterceptHandler(logging.Handler):
    def emit(self, record):
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno
        frame, depth = logging.currentframe(), 2
        while frame.f_code.co_filename == logging.__file__:
            frame = frame.f_back
            depth += 1
        logger.opt(depth=depth, exception=record.exc_info).log(level, record.getMessage())


def logger_init():
    """日志初始化"""
    logging.basicConfig(handlers=[InterceptHandler()], level=0)
    # 详见: https://loguru.readthedocs.io/en/stable/overview.html#features
    logger.add(
        logger_file(),  # 保存日志信息的文件路径
        encoding=settings.GLOBAL_ENCODING,  # 日志文件编码
        level=settings.LOGGER_LEVEL,  # 文件等级
        rotation=settings.LOGGER_ROTATION,  # 日志分片: 按 时间段/文件大小 切分日志. 例如 ["500 MB" | "12:00" | "1 week"]
        retention=settings.LOGGER_RETENTION,  # 日志保留的时间: 超出将删除最早的日志. 例如 ["1 days"]
        enqueue=True  # 在多进程同时往日志文件写日志的时候使用队列达到异步功效
    )
