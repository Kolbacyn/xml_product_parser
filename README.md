[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![GitHub Actions](https://img.shields.io/badge/github%20actions-%232671E5.svg?style=for-the-badge&logo=githubactions&logoColor=white)](https://github.com/features/actions)
[![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&logo=SQLAlchemy&logoColor=SQLAlchemy)](https://www.sqlalchemy.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![Redis](https://img.shields.io/badge/Redis-DC382D?style=for-the-badge&logo=redis&logoColor=white)](https://redis.io/)
[![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![Celery](https://img.shields.io/badge/Celery-3F0B23?style=for-the-badge&logo=celery&logoColor=white)](https://docs.celeryq.dev/en/stable/)
[![OpenAI](https://img.shields.io/badge/OpenAI-000000?style=for-the-badge&logo=openai&logoColor=white)](https://openai.com/)


## xml_product_parser

![Workflow](https://github.com/Kolbacyn/xml_product_parser/actions/workflows/workflow.yml/badge.svg?event=push)

## Описание:

# Микросервис, ежедневно получающий XML-файл с данными о продажах, обрабатывающий его и генерирующий аналитический отчет с помощью LLM.

## Технологии:

- Python 3.12
- FastAPI
- SQLAlchemy
- Alembic
- Redis
- OpenAI
- Docker
- PostgreSQL

## Запуск:

Для начала работы необходимо клонировать репозиторий:

```bash
git clone git@github.com:Kolbacyn/xml_product_parser.git
```

Далее необходимо переходить в директорию проекта:

```bash
cd xml_product_parser
```

Далее необходимо создать виртуальное окружение:

```bash
python3 -m venv venv
```

Далее необходимо активировать виртуальное окружение:

```bash
source venv/bin/activate
```

Создайте файл `.env` в директории проекта:

```bash
touch .env
```

Заполните его данными согласно примеру приведенному в файле `env.example`.

Запуск сервиса:

```bash
docker compose up --build
```

Доступ к документации и приложению:

```bash
http://localhost:8000/docs
```

Перед началом работы с OpenAI необходимо заполнить базу данных минимальными данными и создать отчет, на основании которого будет создаваться аналитика.


## Разработчик

[Зольников Юрий](https://github.com/Kolbacyn/)