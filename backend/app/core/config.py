from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Centralized application settings, loaded from environment variables
    (or a local .env file during development).
    """

    # App
    app_name: str = "Smart Finance Assistant"
    environment: str = "development"

    # Database
    database_url: str = "postgresql://postgres:postgres@localhost:5432/smart_finance"

    # Auth (used starting Phase 2, defined now so .env structure is stable)
    jwt_secret: str = "change-me-in-env"
    jwt_algorithm: str = "HS256"
    access_token_expire_minutes: int = 60

    # AI (used starting Phase 8)
    openai_api_key: str = ""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()