from pydantic_settings import BaseSettings, SettingsConfigDict
from .services_settings import BASE_DIRECTORY




class SettingsId(BaseSettings):
    model_config =  SettingsConfigDict(secrets_dir= BASE_DIRECTORY / "secrets")
    alphavite : str
    upper_limit_of_numbers : str