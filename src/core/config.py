from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str
    ENV: str

    class Config:
        env_file = ".env.test"


settings = Settings()


# SI de casualidad debemos leer variables en pleto Pipeline de CI, debemos colocarlo asi:
# from pydantic_settings import BaseSettings

# class Settings(BaseSettings):
#     DATABASE_URL: str
#     ENV: str

# settings = Settings()
