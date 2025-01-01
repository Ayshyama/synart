from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    api_token: str
    backend_url: str

    class Config:
        env_file = ".env"  # Specify the environment file to load variables
