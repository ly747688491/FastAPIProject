import uvicorn

from apps.main import app

# 运行项目：开发模式

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)