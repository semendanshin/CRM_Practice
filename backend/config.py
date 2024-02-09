from pydantic_settings import BaseSettings
from pydantic import SecretStr


class Settings(BaseSettings):
    JWT_SECRET: SecretStr
    ACCESS_EXPIRE_DAYS: int
    REFRESH_EXPIRE_DAYS: int

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


config = Settings()
