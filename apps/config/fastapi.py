# 配置文件：DbConfig
class FastapiConfig:
    debug = True
    title = '邹丽莎毕设项目'
    description = '基于FastAPI毕设项目'
    version = '0.0.1'
    openapi_url = '/openapi.json'
    openapi_prefix = ''
    docs_url = '/docs'
    redoc_url = '/redoc'
    swagger_ui_oauth2_redirect_url = '/docs/oauth2-redirect'
    swagger_ui_init_oauth = None
    res_path = 'res'
    request_log_to_mongo = False
