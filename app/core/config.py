from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_title: str = 'App title'
    app_version: str = '1.0.0'

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


settings = Settings()
