from .types import TicketCreate, TicketResponse
from aiokafka import AIOKafkaProducer
import asyncio
import json
import os
from random import randint
from config import KAFKA_BOOTSTRAP_SERVERS, KAFKA_TOPIC


class TicketRepo:
    BASE_URL = ""
    KAFKA_URL = KAFKA_BOOTSTRAP_SERVERS
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    
    @classmethod
    async def _post_to_queue(cls, data: dict) -> None:
        producer = AIOKafkaProducer(
            bootstrap_servers=cls.KAFKA_URL)  # объект который изготавливает сообщения кафки
        await producer.start()
        try:
            value = {'data': data}
            print(f'Sending message with value: {value}')
            value_json = json.dumps(value).encode('utf-8')  # преобразуем value в json строку
            await producer.send_and_wait(KAFKA_TOPIC, bytes(value_json))  # отправляет сообщение
        finally:
            # wait for all pending messages to be delivered or expire.
            await producer.stop()
    
    @classmethod
    async def _get(cls, url: str, params: dict = None, headers: dict = None):
        if not params: params = params if params else dict()
        if not headers: headers = dict()
        
        headers |= cls.headers
        
        # async with httpx.AsyncClient(follow_redirects=True) as client:
        #     response = await client.get(
        #         self.BASE_URL+url,
        #         params=params,
        #         headers=headers
        #     )
        #
        # response.raise_for_status() #если не 200 то поднялось исключение
        #
        # return response.json()
        
        return [
            {
                'description': 'все плохо спасите куда я жмал',
                'status': 'в обработке'
            }
        ]
    
    @classmethod
    async def create_ticket(cls, ticket: TicketCreate):
        await cls._post_to_queue(data=ticket.model_dump())
    
    @classmethod
    async def get_all(cls, token: str) -> list[TicketResponse]:
        url = 'tickets'
        headers = {
            'access_token': token,
        }
        response = await cls._get(
            url,
            headers=headers
        )
        return [TicketResponse.model_validate(x) for x in response]
    
    @classmethod
    async def create(cls, ticket: TicketCreate):
        data = ticket.dict()
        await cls._post_to_queue(data)


tickets_collection = TicketRepo

if __name__ == '__main__':
    import asyncio
    
    print(asyncio.run(TicketRepo().get_tickets('jhdcbja')))
