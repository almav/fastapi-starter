from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from src.config.env import ROOT_PATH, RELEASE, TITLE, DESCRIPTION
from src.routers import default

app = FastAPI(root_path=ROOT_PATH, title=TITLE, version=RELEASE, description=DESCRIPTION)

# Inicializar o objeto StaticFiles
app.mount(f"/assets", StaticFiles(directory="public"), name="assets")

# <---- Rotas da aplicação default ---->
app.include_router(default.router)