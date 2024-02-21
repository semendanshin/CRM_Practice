import json
import traceback
from logging import getLogger

from aiokafka import ConsumerRecord
from pydantic import BaseModel, ValidationError

from classificator import Classificator
from crud import BotAuthRepo, TicketTypeRepo, TicketRepo
from db import sessionmaker
from schemas import TicketCreate

logger = getLogger(__name__)


class Message(BaseModel):
    token: str
    description: str


async def create_ticket_handler(message: ConsumerRecord) -> None:
    try:
        parsed_message = await parse_message(message.value)
    except ValidationError as e:
        tb_list = traceback.format_exception(None, e, e.__traceback__)
        tb_string = ''.join(tb_list)
        logger.error(
            f"Error when trying to parse message: {tb_string}"
        )
        return

    logger.info(f"Consume message: {parsed_message}")

    try:
        await create_ticket(parsed_message)
    except Exception as e:
        tb_list = traceback.format_exception(None, e, e.__traceback__)
        tb_string = ''.join(tb_list)

        logger.error(
            f"Error when trying to create ticket ({parsed_message}):\n{tb_string}"
        )
        return


async def parse_message(message: bytes) -> Message:
    return Message.model_validate(json.loads(message.decode("utf-8")))


async def create_ticket(message: Message):
    logger.info(f"Create ticket with description: {message.description}")

    async with sessionmaker() as session:

        if not (bot_auth := await BotAuthRepo.get_by_token(
            session, message.token
        )):
            logger.error(f"Token {message.token} not found.")
            return

        ticket_type_str = await Classificator.classify(message.description)
        logger.info(f"Classificator response: {ticket_type_str}")

        if not (ticket_type := await TicketTypeRepo.get_by_name(
            session, ticket_type_str
        )):
            ticket_type = await TicketTypeRepo.create(
                session, name=ticket_type_str
            )
            logger.info(f"Created new ticket type {ticket_type_str}.")

        ticket = TicketCreate(
            description=message.description,
            client_id=bot_auth.client_id,
            status_id=1,
            type_id=ticket_type.id,
            employee_id=1,
            client_agreement_id=1,
        )

        response = await TicketRepo.create(
            session, **ticket.model_dump()
        )

        logger.info(f"Ticket created: {response}")
