from logging import getLogger

from fastapi import FastAPI

from routes import router

from crud.ClientRepo import ClientRepo
from crud.DeviceRepo import DeviceRepo

logger = getLogger(__name__)


def build_app() -> FastAPI:
    fast_api_app = FastAPI()
    fast_api_app.include_router(router)
    return fast_api_app


app = build_app()
