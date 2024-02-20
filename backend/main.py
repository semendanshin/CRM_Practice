from fastapi import FastAPI

from config import config
from routes import router
from kafka import KafkaTopicListener, create_ticket_handler

from contextlib import asynccontextmanager

import logging

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.DEBUG,
    handlers=[
        # RotatingFileHandler("logs/bot.log", maxBytes=200000, backupCount=5),
        logging.StreamHandler(),
    ]
)
logging.getLogger("httpx").setLevel(logging.WARNING)
logging.getLogger("aiokafka").setLevel(logging.INFO)


logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    listener = KafkaTopicListener(
        config.KAFKA_BOOTSTRAP_SERVERS,
        group_id='group1'
    )
    listener.assign(config.KAFKA_TOPIC, create_ticket_handler)
    await listener.start()

    logger.info("Starting up")

    yield

    logger.info("Shutting down")

    await listener.stop()


def build_app() -> FastAPI:
    fast_api_app = FastAPI(lifespan=lifespan)
    fast_api_app.include_router(router)
    return fast_api_app


app = build_app()
