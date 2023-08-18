import abc
from typing import Optional,Type
from myapp.settings.service_id_settings import SettingsId



class IAttributeManager(abc.ABC):


    @abc.abstractmethod
    def make_attrubutes(self, ttribute_container:Optional[Type[SettingsId]] = None) -> None:
        raise NotImplementedError
    
