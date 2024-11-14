from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_title: str = 'App title'
    app_version: str = '1.0.0'
    database_url: str
    postgres_db: str
    postgres_user: str
    postgres_password: str
    db_host: str
    db_port: int
    openai_api_key: str
    openai_api_url: str
    celery_broker_url: str
    celery_result_backend: str

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


settings = Settings()
