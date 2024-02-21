# CRM_Practice
___

## Описание
Проект представляет собой практикум по созданию CRM системы для компании, занимающейся out-source IT поддержкой.

___

## Сущности

<img alt="ERD" src=".github/db-diagram.png" style="width: auto; height: auto; max-width: 400px;">

## Сервисы

- 'backend' - сервис, отвечающий за взаимодействие с базой данных и бизнес-логику
- 'ml' - сервис, отвечающий за категоризацию новых заявок
- 'client-bot' - телеграмм-бот, отвечающий за прием новых заявок
- 'frontend' - сервис, отвечающий за визуализацию данных и взаимодействие с сотрудниками


___

## Технологии

- FastAPI
- Nginx
- PostgreSQL
- Kafka
- Docker и Docker-compose
- python-telegram-bot

___