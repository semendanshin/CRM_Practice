from pydantic_settings import BaseSettings
from pydantic import SecretStr


class Settings(BaseSettings):
    JWT_SECRET: SecretStr
    ACCESS_EXPIRE_DAYS: int
    REFRESH_EXPIRE_DAYS: int
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASSWORD: SecretStr
    DB_NAME: str

    @property
    def db_uri(self):
        return f'postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD.get_secret_value()}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


config = Settings()
