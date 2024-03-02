class LoginException(Exception):
    """ 登录错误，包含验证码失效、验证码错误、用户名密码错误"""

    def __init__(self, err_desc: str = "用户名、密码、验证码错误或token失效"):
        self.err_desc = err_desc


class AccessTokenFail(Exception):
    """ 访问令牌失败 """

    def __init__(self, err_desc: str = "访问令牌失败"):
        self.err_desc = err_desc


class DataNotExist(Exception):
    """ 存在异常"""

    def __init__(self, err_desc: str = "数据不存在"):
        self.err_desc = err_desc


class CommonException(Exception):
    """ 操作异常"""

    def __init__(self, err_desc: str = "操作异常"):
        self.err_desc = err_desc


class PermissionNotEnough(Exception):
    """ 权限不足,拒绝访问 """

    def __init__(self, err_desc: str = "权限不足,拒绝访问"):
        self.err_desc = err_desc
