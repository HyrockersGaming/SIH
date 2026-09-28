from pydantic import BaseModel


class Settings(BaseModel):
    app_name: str = "T0RI"
    app_env: str = "development"
    debug: bool = True
    secret_key: str = "change-me"


settings = Settings()
