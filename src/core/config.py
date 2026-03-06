from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    ENV: str

    class Config:
        env_file = ".env.test"

settings = Settings()
