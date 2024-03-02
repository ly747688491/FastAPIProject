from fastapi import Request, Response
from loguru import logger
from orjson import orjson
from starlette.responses import StreamingResponse

from models.oper_log import OperLogDb


class OperLogService:

    def __init__(self, request: Request, response: StreamingResponse):
        self.request: Request = request
        self.response: StreamingResponse = response

    async def log_oper(self) -> Response:
        oper_log_sch = self.request.scope.get("oper_log_json", None)
        if oper_log_sch:
            body = b""
            async for chunk in self.response.body_iterator:
                body += chunk
            # do something with body ...
            try:
                oper_log_sch.jsonResult = body
                # 解析并查看code，500则添加错误原因
                result_dict = orjson.loads(body)
                code = result_dict.get("code", 200)
                if code == 200:
                    oper_log_sch.status = "0"
                else:
                    oper_log_sch.status = "1"
                    oper_log_sch.errorMsg = result_dict.get("msg", "")
                # 保存到数据库
                await OperLogDb.create(**oper_log_sch.dict(exclude_none=True))
            except Exception as e:
                logger.error(e)
            finally:
                return Response(
                    content=body,
                    status_code=self.response.status_code,
                    headers=dict(self.response.headers),
                    media_type=self.response.media_type
                )
        else:
            return self.response
