from fastapi import FastAPI

from classifiers import KNeighbours, SGDClassifier, YandexGPTClassifier
from dotenv import load_dotenv

import os

import nltk

nltk.download('stopwords')
nltk.download('punkt')


load_dotenv()

yandex_gpt = YandexGPTClassifier(iam_token=os.getenv("IAM_TOKEN"), folder_id=os.getenv("FOLDER_ID"))
sgd = SGDClassifier()
knb = KNeighbours()

app = FastAPI()


@app.post("/spell_checker")
async def spell_checker(text: str):
    return await yandex_gpt.spell_checker(text)


@app.post("/classify/kneighbours")
async def classify_knb(prompt: str):
    return await knb.predict(prompt)


@app.post("/classify/sgd")
async def classify_sgd(prompt: str):
    return await sgd.predict(prompt)


@app.post("/classify/yandex_gpt")
async def classify_yandex_gpt(prompt: str):
    return await yandex_gpt.identify_category(prompt)
