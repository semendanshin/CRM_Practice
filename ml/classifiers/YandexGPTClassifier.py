from httpx import AsyncClient

from .AbstractClassifier import AbstractClassifier
from .types import HumanReadableResponse


class YandexGPTClassifier(AbstractClassifier):
    URL = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"

    CLASSIFICATION_PROMPT = ("Классифицируй обращения клиента в подходящую категорию. "
                             "Выбери из категорий: «Инцидент», «Запрос на обслуживание», «Выезд», "
                             "«Внутренняя помощь», «Проект», «Поставка», «Проблема», «Задача». "
                             "В ответе укажи только категорию в формате: Инцидент"
                             "без дополнительных слов/символов!")
    SPELL_CHECKER_PROMPT = ("Ты — оператор клиентской поддержки и тебе поступают запросы от клиентов. "
                            "Переформулируй запросы так, чтобы сохранялся их смысл, "
                            "но при этом их было легче читать. "
                            "На выходе требуется один вариант переформулированного запроса"
                            "без дополнительных символов!")

    def __init__(self, iam_token: str, folder_id: str):
        self.iam_token = iam_token
        self.folder_id = folder_id
        self.headers = {
            "Authorization": f"Bearer {self.iam_token}",
            "x-folder-id": self.folder_id,
        }

    def _make_payload(self, user_text, system_text):
        return {
            "modelUri": f"gpt://{self.folder_id}/yandexgpt-lite",
            "completionOptions": {
                "stream": False,
                "temperature": 0,
                "maxTokens": "2000"
            },
            "messages": [
                {
                    "role": "system",
                    "text": system_text
                },
                {
                    "role": "user",
                    "text": user_text
                }
            ]
        }

    async def _post(self, url: str, headers: dict = None, json: dict = None):
        headers = headers if headers else {}
        json = json if json else {}
        headers.update(self.headers)
        async with AsyncClient() as client:
            response = await client.post(url, headers=headers, json=json)
            response.raise_for_status()
            return response.json()

    async def _make_prompt(self, user_text, system_text):
        result = await self._post(self.URL, json=self._make_payload(user_text, system_text))
        return result['result']['alternatives'][0]['message']['text']

    async def spell_checker(self, user_text: str):
        return await self._make_prompt(user_text, self.SPELL_CHECKER_PROMPT)

    async def identify_category(self, user_text: str):
        return await self._make_prompt(user_text, self.CLASSIFICATION_PROMPT)

    async def predict(self, text: str):
        processed_text = await self.spell_checker(text)
        response = await self.identify_category(
            processed_text
        )
        return HumanReadableResponse(response)
