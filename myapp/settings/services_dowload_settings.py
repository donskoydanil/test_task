from pydantic_settings import BaseSettings, SettingsConfigDict
from services_settings import BASE_DIRECTORY





class ServicesDownloadSettings(BaseSettings):
    model_config =  SettingsConfigDict(secrets_dir= BASE_DIRECTORY / "secrets")
    
    url : str


services_download_settings = ServicesDownloadSettings() 
