from config import config
from httpx import AsyncClient
from typing import Literal


class Classificator:
    base_url = config.CLASSIFICATOR_URL

    @classmethod
    async def _post(cls, url, params, data: dict = None):
        data = data if data else {}
        async with AsyncClient() as client:
            response = await client.post(f"{cls.base_url}{url}", params=params, json=data)
            response.raise_for_status()
            return response.json()

    @classmethod
    async def classify(cls, text: str, classifier: Literal["kneighbours", "sgd", "yandex_gpt"] = "yandex_gpt") -> str:
        url = "/classify/" + classifier
        data = {"text": text}
        response = await cls._post(url, data)
        print(response)
        return response
