import requests
from dotenv import load_dotenv
import os
import asyncio
import time


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


def spell_checker(user_text):
    sys_msg = "Ты — оператор клиентской поддержки и тебе поступают запросы от клиентов. Переформулируй запросы так, чтобы сохранялся их смысл, но при этом их было легче читать. На выходе требуется один вариант переформулированного запроса!"
    return prompt(user_text, sys_msg)


def identify_category(user_text):
    try:
        sys_msg = "Классифицируй обращения клиента в подходящую категорию. Категории: «Инцидент», «Запрос на обслуживание», «Выезд», «Внутренняя помощь», «Проект», «Поставка», «Проблема», «Задача». В ответе укажи только категорию в формате: Инцидент."
        processed_text = spell_checker(user_text)
        return prompt(processed_text, sys_msg)
    except KeyError:
        sys_msg = "Классифицируй обращения клиента в подходящую категорию. Категории: «Инцидент», «Запрос на обслуживание», «Выезд», «Внутренняя помощь», «Проект», «Поставка», «Проблема», «Задача». В ответе укажи только категорию в формате: Инцидент."
        processed_text = spell_checker(user_text)
        time.sleep(0.5)
        return prompt(processed_text, sys_msg)
