from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_title: str = 'App title'
    app_version: str = '1.0.0'
    database_url: str = 'postgresql+asyncpg://postgres:postgres@db:5432/fastap'
    postgres_db: str = 'fastapi'
    postgres_user: str = 'postgres'
    postgres_password: str = 'postgres'
    db_host: str = 'db'
    db_port: int = 5432
    openai_api_key: str = 'Ваш ключ доступа к APi'
    openai_api_url: str = 'https://openapi'
    celery_broker_url: str = 'redis://guest:guest@localhost:6379'
    celery_result_backend: str = 'redis://guest:guest@localhost:6379'

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


settings = Settings()
