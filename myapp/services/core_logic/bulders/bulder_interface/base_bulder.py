import abc
from typing import Type


class BaseBulder(abc.ABC):
        
        
    @abc.abstractproperty
    @property
    def ready_instanse(self) -> Type:
        raise NotImplementedError
