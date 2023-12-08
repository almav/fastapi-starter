# FastAPI Starter

* version 0.0.1
* description FastAPI Starter for Nginx
* author Jeifferson R. Moraes
* license Apache-2.0
* tags python fastapi starter nginx

## ROOT_PATH

Você deve configurar o ```ROOT_PATH``` para o caminho da sua aplicação.

Edite o arquivo: [./src/config/env.py](./src/config/env.py)

Exemplo:
```shell
# Nome público da aplicação definida no Nginx: '/v1'
# Exemplo: https://domain/v1
ROOT_PATH='/v1'
```

## Módulo Principal

Definir como: ```src.main:app```

* ```src:``` É o diretório da sua aplicação.
* ```main:``` É o nome do módulo principal.
* ```app:``` É o objeto ou função principal.

Exemplo: 

```app = FastAPI(root_path=ROOT_PATH)```

## Test
```uvicorn src.main:app --reload```

## Deploy
```shell
su stageApiLogin_almav
# pull github
git pull origin main
# se necessário, reinicie o serviço
sudo /usr/bin/systemctl restart stage.api.login.almav.com-r1.service
```
