import os
from decouple import Csv, Config, config

env_path = os.path.join(os.path.dirname(__file__), '..', '.env')

# Verifique se o arquivo .env existe
config_instance = Config(env_path) if os.path.exists(env_path) else config

# Nome público da aplicação definida no Nginx: '/' + $app_conf_name
# Exemplo: https://domain/v1, sendo ROOTH_PATH='/v1'
ROOT_PATH = config_instance('ROOT_PATH', default=os.environ.get('ROOT_PATH', '/'))
MODE = config_instance('MODE', default=os.environ.get('MODE', 'development'))

# Version
RELEASE = config_instance('RELEASE', default=os.environ.get('RELEASE', 'v0.0.1-beta'))
RELEASE_CREATED_AT = config_instance('RELEASE_CREATED_AT', default=os.environ.get('RELEASE_CREATED_AT', '2023-12-07'))
TITLE = config_instance('TITLE', default=os.environ.get('TITLE', 'almav'))
DESCRIPTION = config_instance('DESCRIPTION', default=os.environ.get('DESCRIPTION', 'FastAPI Nginx VHOST'))