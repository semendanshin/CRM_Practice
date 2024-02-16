import asyncio

from fastapi import FastAPI

from routes import router
from kafka import consume

from contextlib import asynccontextmanager

import logging

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    handlers=[
        # RotatingFileHandler("logs/bot.log", maxBytes=200000, backupCount=5),
        logging.StreamHandler(),
    ]
)
logging.getLogger("httpx").setLevel(logging.WARNING)


logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    loop = asyncio.get_running_loop()
    task = loop.create_task(consume())
    logger.info("Starting up")
    yield
    logger.info("Shutting down")
    task.cancel()


def build_app() -> FastAPI:
    fast_api_app = FastAPI(lifespan=lifespan)
    fast_api_app.include_router(router)
    return fast_api_app


app = build_app()
