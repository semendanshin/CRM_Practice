import asyncio
import traceback
from logging import getLogger
from typing import Coroutine, Callable, Any, Optional

from aiokafka import AIOKafkaConsumer, ConsumerRecord


logger = getLogger(__name__)


Handler = Callable[[ConsumerRecord], Coroutine[Any, Any, None]]


class KafkaTopicListener:
    def __init__(
            self,
            bootstrap_servers: str = 'localhost',
            group_id: str = 'group',
            periodicity: int = 5,
    ):
        self._bootstrap_servers = bootstrap_servers
        self._group_id = group_id
        self._periodicity = periodicity

        self._is_running = False

        self._consumer: Optional[AIOKafkaConsumer] = None
        self._loop: Optional[asyncio.AbstractEventLoop] = None

        self._handlers: dict[str, Handler] = {}

    async def start(self):
        if self._is_running:
            logger.warning("Consumer is already running.")
        await self._start()

    async def _initialize(self):
        self._loop = asyncio.get_running_loop()
        self._consumer = AIOKafkaConsumer(
            *self._handlers.keys(),
            bootstrap_servers=self._bootstrap_servers,
            enable_auto_commit=True,
            auto_commit_interval_ms=1000,
            auto_offset_reset="earliest",
            group_id=self._group_id,
        )

    async def _start(self):
        if self._consumer is None:
            await self._initialize()

        await self._consumer.start()

        self._is_running = True

        self._loop.create_task(self._consume())

        logger.info("Consumer started.")

    async def stop(self):
        if not self._is_running:
            logger.warning("Consumer is not running.")
        await self._stop()

    async def _stop(self):
        self._is_running = False
        await self._consumer.stop()
        logger.info("Consumer stopped.")

    async def _consume(self):
        if not self._is_running or self._consumer is None:
            raise Exception("Consumer is not running.")

        while self._is_running:
            result = await self._consumer.getmany(
                timeout_ms=1000, max_records=5
            )

            logger.debug(f"Get {len(result)} messages.")

            for tp, messages in result.items():
                if not messages:
                    continue

                if not (handler := self._handlers.get(tp.topic)):
                    logger.error(f"No handler for topic: {tp.topic}")
                    continue

                for message in messages:
                    try:
                        result = self._loop.create_task(handler(message))
                    except Exception as e:
                        tb_list = traceback.format_exception(None, e, e.__traceback__)
                        tb_string = ''.join(tb_list)

                        logger.error(
                            f"Error when trying to parse message: {message}\n{tb_string}"
                        )
                        continue

                    logger.debug(f"Success consume message: {message} with result: {result}")

                await self._consumer.commit({tp: messages[-1].offset + 1})

            await asyncio.sleep(self._periodicity)

    def assign(self, topic: str, handler: Handler):
        self._handlers[topic] = handler
