# AutoSnab API

REST API сервис для обработки запросов по кадастровым данным.

Проект выполнен в рамках практического задания компании **«Автоснаб» («Antipoff Group»)**.

## Описание проекта

Сервис принимает запрос с кадастровым номером объекта и его координатами (широта и долгота), отправляет запрос на эмуляцию внешнего сервера, получает результат проверки (`true` или `false`) и сохраняет информацию о запросе и ответе в базе данных PostgreSQL.

Также реализовано получение истории всех запросов и поиск истории по кадастровому номеру.

## Реализованный функционал

В проекте реализованы следующие возможности:

* проверка состояния сервера и подключения к базе данных;
* создание запроса проверки кадастрового объекта;
* эмуляция внешнего сервера;
* сохранение данных запроса и результата ответа в PostgreSQL;
* получение истории запросов;
* фильтрация истории по кадастровому номеру;
* асинхронная работа с базой данных;
* миграции базы данных через Alembic;
* запуск приложения через Docker Compose;
* автоматическое тестирование API.

---

# Технологии

* Python 3.9+
* FastAPI
* SQLAlchemy 2.0 Async
* asyncpg
* PostgreSQL 16
* Alembic
* Pydantic
* Docker
* Docker Compose
* Pytest
* Uvicorn

---

# Структура проекта

```
autosnab/
│
├── app/
│   ├── api/
│   │   ├── ping.py
│   │   ├── query.py
│   │   ├── history.py
│   │   └── result.py
│   │
│   ├── core/
│   ├── db/
│   ├── schemas/
│   ├── services/
│   └── main.py
│
├── migrations/
│
├── tests/
│   ├── conftest.py
│   ├── test_ping.py
│   └── test_query.py
│
├── alembic.ini
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

# Запуск проекта

## 1. Клонирование репозитория

```bash
git clone <repository_url>

cd autosnab
```

---

## 2. Настройка переменных окружения

Создать файл `.env`:

```env
DB_HOST=localhost
DB_PORT=5433
DB_NAME=autosnab_db
DB_USER=autosnab_user
DB_PASSWORD=autosnab_password
```

---

## 3. Запуск через Docker Compose

Сборка и запуск приложения:

```bash
docker compose up --build
```

После успешного запуска API доступно:

```
http://127.0.0.1:8000
```

Swagger документация:

```
http://127.0.0.1:8000/docs
```

---

## 4. Остановка проекта

Остановить контейнеры:

```bash
docker compose down
```

Удалить контейнеры вместе с данными PostgreSQL:

```bash
docker compose down -v
```

---

# API Endpoints

## Проверка сервера

### GET `/ping`

Проверяет, что приложение запущено и есть подключение к базе данных.

Пример ответа:

```json
{
  "database": 1
}
```

---

# Создание запроса

## POST `/query`

Создание запроса проверки кадастрового объекта.

Принимает:

* кадастровый номер;
* широту;
* долготу.

Пример запроса:

```json
{
  "cadastral_number": "77:01:0000000:123",
  "latitude": 55.7558,
  "longitude": 37.6173
}
```

Пример ответа:

```json
{
  "cadastral_number": "77:01:0000000:123",
  "result": false
}
```

Логика работы:

```
POST /query
       |
       ↓
Отправка запроса во внешний сервис /result
       |
       ↓
Получение результата true/false
       |
       ↓
Сохранение данных в PostgreSQL
       |
       ↓
Ответ пользователю
```

---

# История запросов

## GET `/history`

Получение всех запросов:

```
/history
```

Получение истории по кадастровому номеру:

```
/history?cadastral_number=77:01:0000000:123
```

Пример ответа:

```json
[
  {
    "id": 1,
    "cadastral_number": "77:01:0000000:123",
    "latitude": 55.7558,
    "longitude": 37.6173,
    "result": false,
    "created_at": "2026-07-28T10:18:38"
  }
]
```

---

# Эмуляция внешнего сервера

## POST `/result`

Эндпоинт имитирует внешний сервис.

Получает данные:

```json
{
  "cadastral_number": "77:01:0000000:123",
  "latitude": 55.7558,
  "longitude": 37.6173
}
```

Возвращает результат проверки:

```json
{
  "result": true
}
```

---

# База данных

Используется:

* PostgreSQL 16;
* SQLAlchemy Async;
* asyncpg.

Миграции выполняются через Alembic.

Применение миграций:

```bash
alembic upgrade head
```

Создание новой миграции:

```bash
alembic revision --autogenerate -m "migration_name"
```

---

# Тестирование

Запуск тестов:

```bash
python -m pytest -v
```

Проверяются:

* доступность эндпоинта `/ping`;
* создание запроса через `/query`;
* корректность ответов API.

---

# Docker

Используются контейнеры:

```
autosnab-backend
```

FastAPI приложение.

```
autosnab-postgres
```

PostgreSQL база данных.

Проверка запущенных контейнеров:

```bash
docker ps
```

Просмотр логов PostgreSQL:

```bash
docker logs autosnab-postgres
```

---

# Документация API

После запуска доступна автоматическая документация Swagger:

```
http://127.0.0.1:8000/docs
```

---

# Автор

Гюнай Меджидова
