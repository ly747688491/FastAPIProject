from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


def register_cors(app: FastAPI):
    """
    跨域请求 -- https://fastapi.tiangolo.com/zh/tutorial/cors/
    https://www.cnblogs.com/poloyy/p/15347578.html
    """

    app.add_middleware(
        CORSMiddleware,
        # allow_origins=[str(origin) for origin in settings.CORS_ORIGINS], # 允许访问的源
        allow_origins=["*"],  # 允许访问的源
        allow_credentials=True,  # 支持 cookie
        allow_methods=("GET", "POST", "PUT", "DELETE"),  # 允许使用的请求方法
        allow_headers=("*", "authentication"),  # 允许携带的 Headers
    )
