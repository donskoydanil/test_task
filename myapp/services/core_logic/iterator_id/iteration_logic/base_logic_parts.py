import abc
from typing import Any,Optional,Type
from myapp.settings.service_id_settings import SettingsId




class BaseIteratorLogic:

    @abc.abstractmethod
    def _make_iterator_logic_attrubutes(self) -> None:
        raise NotImplementedError
    
    @abc.abstractmethod
    def __next__(self) -> Any:
        raise NotImplementedError
    


class IAttributeManager(abc.ABC):


    @abc.abstractmethod
    def make_attrubutes(self, ttribute_container:Optional[Type[SettingsId]] = None) -> None:
        raise NotImplementedError