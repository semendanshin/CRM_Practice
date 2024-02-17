import asyncio
import json
from logging import getLogger

from aiokafka import AIOKafkaConsumer
from pydantic import BaseModel, ValidationError
from sqlalchemy.ext.asyncio import AsyncSession

from classificator_repo import Classificator
from config import config
from crud import TicketRepo, BotAuthRepo, TicketTypeRepo
from db import get_session
from schemas import TicketCreate
from traceback import print_exception

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
                        try:
                            parsed_message = await parse_message(message.value)
                        except ValidationError as e:
                            logger.error(
                                f"Error when trying to parse message: {print_exception(e)}"
                            )
                            continue

                        logger.info(f"Consume message: {parsed_message}")

                        try:
                            await create_ticket(parsed_message)
                        except Exception as e:
                            logger.error(
                                f"Error when trying to create ticket ({parsed_message}): {print_exception(e)}"
                            )
                            continue

                    await consumer.commit({tp: messages[-1].offset + 1})
            await asyncio.sleep(5)
    except Exception as e:
        logger.error(
            f"Error when trying to consume request on topic {config.KAFKA_TOPIC}: {print_exception(e)}"
        )
        raise e
    finally:
        await consumer.stop()


async def parse_message(message: bytes) -> Message:
    return Message.model_validate(json.loads(message.decode("utf-8")))


async def create_ticket(message: Message):
    logger.info(f"Create ticket with description: {message.description}")
    session: AsyncSession = await get_session().__anext__()
    bot_auth = await BotAuthRepo.get_by_token(
        session, message.token
    )

    if bot_auth is None:
        logger.error(f"Token {message.token} not found.")
        return

    client_id = bot_auth.client_id

    type_str = await Classificator.classify(message.description)
    logger.info(f"Classificator response: {type_str}")

    types = await TicketTypeRepo.get_filtered_by(
        session, name=type_str
    )

    if not types:
        new_type = await TicketTypeRepo.create(
            session, name=type_str
        )

        logger.info(f"Created new ticket type {type_str}.")
        type_id = new_type.id
    else:
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
