from myapp.services.core_logic.iterator_logic.iterator_logic_interface import BaseIteratorLogic
from myapp.services.core_logic.iterator_id.iterator_id import IteratorId
from myapp.services.core_logic.bulders.bulder_iterator_logic.bulder_iterator_logic import IteratorLogicBulder
from myapp.services.core_logic.bulders.bulder_iterator_id.bulder_iterator_id import IteratorIdBulder

class MakeIteratorId:

    def __init__(self,
                bulder_iterator_logic : IteratorLogicBulder,
                bulder_iterator_id : IteratorIdBulder
                ) -> None:
        self.bulder_iterator_logic = bulder_iterator_logic
        self.bulder_iterator_id = bulder_iterator_id

    def _make_iterator_logic(self) -> BaseIteratorLogic:
        return self.bulder_iterator_logic().ready_instanse
    
    def _make_iterator_id(self, ready_iterator_logic:BaseIteratorLogic) ->IteratorId:
        return self.bulder_iterator_id(ready_iterator_logic).ready_instanse
    

    def make_ready_iterator_id(self) ->IteratorId:
        iterator_logic = self._make_iterator_logic()
        iterator_id = self._make_iterator_id(iterator_logic)

        return iterator_id

        