from pydantic_settings import BaseSettings
from pathlib import Path

class Settings(BaseSettings):
    database_hostname: str
    database_port: str
    database_password: str
    database_name: str
    database_username: str
    secret_key: str
    algorithm: str
    oauth2_scheme: str = "Bearer"  



    class Config:
        env_file = Path("/home/nevin/Documents/arya/famfin-back/.env")


settings = Settings(_env_file=Path("/home/nevin/Documents/arya/famfin-back/.env"), _env_file_encoding="utf-8")