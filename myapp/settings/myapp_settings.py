from pathlib import Path 
from pydantic_settings import BaseSettings, SettingsConfigDict




BASE_DIRECTORY = Path(__file__).absolute().parent.parent


class ServicesDownloadSettings(BaseSettings):
    model_config =  SettingsConfigDict(secrets_dir= BASE_DIRECTORY / "secrets")
    
    url : str


services_download_settings = ServicesDownloadSettings(_secrets_dir= BASE_DIRECTORY / "secrets") 

