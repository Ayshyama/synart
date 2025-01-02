from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    API_TOKEN: str
    BACKEND_URL: str

    class Config:
        env_file = ".env"  # Specify the environment file to load variables
