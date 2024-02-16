from enum import Enum


class Response(Enum):
    INCIDENT = 0
    SERVICE_REQUEST = 1
    VISIT = 2
    INTERNAL_SUPPORT = 3
    PROJECT = 4
    DELIVERY = 5
    PROBLEM = 6
    TASK = 7


class HumanReadableResponse(Enum):
    INCIDENT = "Инцидент"
    SERVICE_REQUEST = "Запрос на обслуживание"
    VISIT = "Выезд"
    INTERNAL_SUPPORT = "Внутренняя помощь"
    PROJECT = "Проект"
    DELIVERY = "Поставка"
    PROBLEM = "Проблема"
    TASK = "Задача"
