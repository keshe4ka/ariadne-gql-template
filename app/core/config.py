from pydantic import BaseSettings, PostgresDsn, RedisDsn, AnyHttpUrl


class Settings(BaseSettings):
    debug: bool
    database_url: PostgresDsn
