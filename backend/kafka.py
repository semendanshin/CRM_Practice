import asyncio
import json
from logging import getLogger

from aiokafka import AIOKafkaConsumer
from pydantic import BaseModel

from classificator_repo import Classificator
from config import config
from crud import TicketRepo, BotAuthRepo, TicketTypeRepo
from db import get_session
from schemas import TicketCreate

logger = getLogger(__name__)


class Message(BaseModel):
    token: str
    description: str


async def consume():
    consumer = AIOKafkaConsumer(
        config.KAFKA_TOPIC,
        bootstrap_servers=config.KAFKA_BOOTSTRAP_SERVERS,
        enable_auto_commit=True,
        auto_commit_interval_ms=1000,
        auto_offset_reset="earliest",
        group_id=config.KAFKA_CONSUMER_GROUP_PREFIX,
    )

    logger.info(
        f"Start consumer on topic '{config.KAFKA_TOPIC}'."
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
                if tp.topic == config.KAFKA_TOPIC and messages:
                    for message in messages:
                        parsed_message = await parse_message(message.value)
                        logger.info(f"Consume message: {parsed_message}")
                        await create_ticket(parsed_message)
                    await consumer.commit({tp: messages[-1].offset + 1})
            await asyncio.sleep(5)
    except Exception as e:
        logger.error(
            f"Error when trying to consume request on topic {config.KAFKA_TOPIC}: {str(e)}"
        )
        raise e
    finally:
        await consumer.stop()


async def parse_message(message: bytes) -> Message:
    return Message.model_validate(json.loads(message.decode("utf-8")))


async def create_ticket(message: Message):
    logger.info(f"Create ticket with description: {message.description}")
    async with get_session() as session:
        client_id = await BotAuthRepo.get_by_token(
            session, message.token
        )

        if client_id is None:
            logger.error(f"Client with token {message.token} not found.")
            return

        type_str = Classificator.classify(message.description)
        logger.info(f"Classificator response: {type_str}")

        types = TicketTypeRepo.get_where(
            session, name=type_str
        )

        if not types:
            logger.error(f"Ticket type {type_str} not found.")
            return

        type_id = types[0].id

        ticket = TicketCreate(
            description=message.description,
            client_id=client_id,
            status_id=1,
            type_id=type_id,
            employee_id=1,
            client_agreement_id=1,
        )

        response = await TicketRepo.create(
            session, **ticket.model_dump()
        )

        logger.info(f"Ticket created: {response}")
