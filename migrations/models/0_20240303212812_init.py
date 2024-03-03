from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS `aerich` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `version` VARCHAR(255) NOT NULL,
    `app` VARCHAR(100) NOT NULL,
    `content` JSON NOT NULL
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `sys_oper_log` (
    `oper_id` BIGINT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `title` VARCHAR(50)   DEFAULT '',
    `business_type` INT   DEFAULT 0,
    `method` VARCHAR(100)   DEFAULT '',
    `request_method` VARCHAR(10)   DEFAULT '',
    `operator_type` INT   DEFAULT 0,
    `oper_name` VARCHAR(50)   DEFAULT '',
    `dept_name` VARCHAR(50)   DEFAULT '',
    `oper_url` VARCHAR(255)   DEFAULT '',
    `oper_ip` VARCHAR(128)   DEFAULT '',
    `oper_location` VARCHAR(255)   DEFAULT '',
    `oper_param` LONGTEXT,
    `json_result` LONGTEXT,
    `status` VARCHAR(1)   DEFAULT '0',
    `error_msg` VARCHAR(2000)   DEFAULT '',
    `oper_time` DATETIME(6)   DEFAULT CURRENT_TIMESTAMP(6)
) CHARACTER SET utf8mb4 COMMENT='操作日志记录';
CREATE TABLE IF NOT EXISTS `job_info` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `position_name` VARCHAR(100) NOT NULL,
    `salary_range` VARCHAR(100) NOT NULL,
    `location` VARCHAR(100) NOT NULL,
    `work_experience` VARCHAR(100) NOT NULL,
    `education_requirement` VARCHAR(100) NOT NULL,
    `position_tag` VARCHAR(100) NOT NULL,
    `company_name` VARCHAR(100) NOT NULL,
    `company_type` VARCHAR(100) NOT NULL,
    `company_size` VARCHAR(100) NOT NULL,
    `province` VARCHAR(100) NOT NULL,
    `city` VARCHAR(100) NOT NULL
) CHARACTER SET utf8mb4 COMMENT='岗位信息表';"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
