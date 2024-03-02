from tortoise import fields
from tortoise.models import Model


class OperLogDb(Model):
    operId = fields.BigIntField(source_field="oper_id", pk=True, describe="日志主键")
    title = fields.CharField(max_length=50, null=True, default="", describe="模块标题")
    businessType = fields.IntField(source_field="business_type", null=True, default=0,
                                   describe="业务类型（0其它 1新增 2修改 3删除）")
    method = fields.CharField(max_length=100, null=True, default="", describe="方法名称")
    requestMethod = fields.CharField(source_field="request_method", max_length=10, null=True, default="",
                                     describe="请求方式")
    operatorType = fields.IntField(source_field="operator_type", null=True, default=0,
                                   describe="操作类别（0其它 1后台用户 2手机端用户）")
    operName = fields.CharField(source_field="oper_name", max_length=50, null=True, default="", describe="操作人员")
    deptName = fields.CharField(source_field="dept_name", max_length=50, null=True, default="", describe="部门名称")
    operUrl = fields.CharField(source_field="oper_url", max_length=255, null=True, default="", describe="请求URL")
    operIp = fields.CharField(source_field="oper_ip", max_length=128, null=True, default="", describe="主机地址")
    operLocation = fields.CharField(source_field="oper_location", max_length=255, null=True, default="",
                                    describe="操作地点")
    operParam = fields.TextField(source_field="oper_param", null=True, default="", describe="请求参数")
    jsonResult = fields.TextField(source_field="json_result", null=True, default="",
                                  describe="返回参数")
    status = fields.CharField(max_length=1, null=True, default="0", describe="操作状态（0正常 1异常）")
    errorMsg = fields.CharField(source_field="error_msg", max_length=2000, null=True, default="", describe="错误消息")
    operTime = fields.DatetimeField(source_field="oper_time", auto_now_add=True, null=True, describe="操作时间")

    class Meta:
        table = "sys_oper_log"
        table_description = "操作日志记录"
