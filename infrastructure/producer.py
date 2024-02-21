from aiokafka import AIOKafkaProducer
import asyncio
import json
import os
from random import randint
from dotenv import load_dotenv

load_dotenv()


# env variables
KAFKA_TOPIC = os.getenv('KAFKA_TOPIC')
KAFKA_BOOTSTRAP_SERVERS = os.getenv('KAFKA_BOOTSTRAP_SERVERS', 'localhost:9092')

# global variables
loop = asyncio.get_event_loop()


async def send_one():
    producer = AIOKafkaProducer(bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS)
    # get cluster layout and initial topic/partition leadership information
    await producer.start()
    try:
        # produce message
        msg_id = f'{randint(1, 10000)}'
        value = {'message_id': msg_id, 'text': 'some text', 'state': randint(1, 100)}
        key = "super_key"
        headers = [("key", "value")]
        print(f'Sending message with value: {value}')
        value_json = json.dumps(value).encode('utf-8')
        await producer.send_and_wait(
            KAFKA_TOPIC,
            value_json,
            key=key.encode('utf-8'),
            headers=[(i[0], i[1].encode('utf-8')) for i in headers]
        )
    finally:
        # wait for all pending messages to be delivered or expire.
        await producer.stop()

# send message
loop.run_until_complete(send_one())
