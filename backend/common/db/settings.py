from pydantic import BaseSettings
from backend.common.core.config import config


class Settings(BaseSettings):
    db_url: str = config["DB_URL"]


settings = Settings()
