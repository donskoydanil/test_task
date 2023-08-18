import abc
from typing import Any



class BaseIteratorLogic:

    @abc.abstractmethod
    def _make_iterator_logic_attrubutes(self) -> None:
        raise NotImplementedError
    
    @abc.abstractmethod
    def __next__(self) -> Any:
        raise NotImplementedError
    

