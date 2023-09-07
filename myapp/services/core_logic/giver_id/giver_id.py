from typing import Iterator,Any
from myapp.services.core_logic.iterator_id.iterator_id import IteratorId

class GiverId:

    def __init__(self,ready_iterator_id:IteratorId) -> None:
        
        self.iterator_id = ready_iterator_id
        self.generator_id = self._make_instanse_of_iterator(self.iterator_id)


    def _make_instanse_of_iterator(self, ready_iterator:IteratorId) ->Iterator:
        return iter(ready_iterator)
    
    def _make_id(self) -> Any:

        try:
            out = next(self.generator_id)
        except StopIteration:
            self.__init__()
            out = next(self.generator_id)

        return out
    
    @property
    def give_id(self) -> Any:

        out_id =  self._make_id()
        return out_id 
    