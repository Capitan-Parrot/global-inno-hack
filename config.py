from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr


class Settings(BaseSettings):
    bot_token: SecretStr

    server_host: str = '127.0.0.1'
    server_port: int = 8000

    postgres_user: str
    postgres_password: str
    postgres_server: str
    postgres_db: str

    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')


config = Settings()