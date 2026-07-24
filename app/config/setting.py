from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    APP_NAME: str
    APP_VERSION: str

    CHROMA_DB_PATH: str

    EMBEDDING_MODEL: str

    UPLOAD_DIR: str


    GEMINI_API_KEY: str

    GEMINI_MODEL: str

    class Config:
        env_file = ".env"


settings = Settings()