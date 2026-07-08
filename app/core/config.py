from pydantic import BaseModel
import os


class Settings(BaseModel):
    APP_NAME: str = "Patel Platform Service Template"
    DEBUG: bool = True
    DATABASE_URL: str = os.getenv(
        "DATABASE_URL",
        "sqlite:///./patel_platform.db"
    )


settings = Settings()