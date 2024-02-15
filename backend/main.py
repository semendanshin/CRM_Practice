from fastapi import FastAPI

from routes.bot.routes import router as bot_router
from routes.auth.routes import router as auth_router

from logging import getLogger

logger = getLogger(__name__)


def build_app() -> FastAPI:
    fast_api_app = FastAPI()
    fast_api_app.include_router(auth_router)
    fast_api_app.include_router(bot_router)
    return fast_api_app


app = build_app()
