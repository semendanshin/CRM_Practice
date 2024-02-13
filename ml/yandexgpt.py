import requests
import json
from dotenv import load_dotenv
import os


def prompt(user_text, system_text):
    load_dotenv()
    iam_token = os.getenv("IAM_TOKEN")
    folder_id = os.getenv("ID_FOLDER")
    url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
    res = requests.request(method="POST", url=url, headers={
        "Authorization": f"Bearer {iam_token}",
        "x-folder-id": folder_id,
    }, json={
        "modelUri": f"gpt://{folder_id}/yandexgpt-lite",
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
    })
    return res.json()['result']['alternatives'][0]['message']['text']


def identify_category(user_text):
    sys_msg = "Классифицируй обращения клиента в подходящую категорию. Категории: «Инцидент», «Запрос на обслуживание», «Выезд», «Внутренняя помощь», «Проект», «Поставка», «Проблема», «Задача». В ответе укажи только категорию."
    return prompt(user_text, sys_msg)
