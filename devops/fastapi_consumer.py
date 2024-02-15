from contextlib import asynccontextmanager

from aiokafka import AIOKafkaConsumer
from fastapi import FastAPI, APIRouter
from dotenv import load_dotenv

import uvicorn
import asyncio
import json
import logging
import os

from logging import getLogger

logger = getLogger(__name__)

load_dotenv()

# instantiate the API
router = APIRouter()

# env variables
KAFKA_TOPIC = os.getenv('KAFKA_TOPIC')
KAFKA_CONSUMER_GROUP_PREFIX = os.getenv('KAFKA_CONSUMER_GROUP_PREFIX', 'group')
KAFKA_BOOTSTRAP_SERVERS = os.getenv('KAFKA_BOOTSTRAP_SERVERS', 'localhost:9092')

# initialize logger
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
log = logging.getLogger(__name__)


async def consume():
    consumer = AIOKafkaConsumer(
        KAFKA_TOPIC,
        bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
        enable_auto_commit=True,
        auto_commit_interval_ms=1000,
        auto_offset_reset="earliest",
        group_id=KAFKA_CONSUMER_GROUP_PREFIX,
    )

    logger.info(
        f"Start consumer on topic '{KAFKA_TOPIC}'."
    )

    await consumer.start()

    logger.info("Consumer started.")

    try:
        while True:
            result = await consumer.getmany(
                timeout_ms=1000, max_records=5
            )

            logger.info(f"Get {len(result)} messages.")

            for tp, messages in result.items():
                if messages:
                    for message in messages:
                        logger.info(
                            {
                                "key": message.key.decode("utf-8") if message.key else None,
                                "value": message.value.decode("utf-8") if message.value else None,
                                "headers": [(key, value.decode("utf-8") if value else None)
                                            for key, value in message.headers],
                            },
                        )
                    await consumer.commit({tp: messages[-1].offset + 1})
            await asyncio.sleep(1)
    except Exception as e:
        logger.error(
            f"Error when trying to consume request on topic {KAFKA_TOPIC}: {str(e)}"
        )
        raise e
    finally:
        await consumer.stop()


@router.get("/")
async def root():
    return {"message": "Hello World"}


@asynccontextmanager
async def lifespan(app: FastAPI):
    loop = asyncio.get_running_loop()
    task = loop.create_task(consume())
    logger.info("Starting up")
    yield
    logger.info("Shutting down")
    task.cancel()


if __name__ == "__main__":
    app = FastAPI(lifespan=lifespan, debug=True)
    app.include_router(router)
    uvicorn.run(app, host="0.0.0.0", port=8000)
