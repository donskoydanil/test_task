from typing import Optional
from myapp.services.core_logic.maker_of_iterator_id.maker_iterator_id import MakeIteratorId
from myapp.services.core_logic.bulders.bulder_iterator_logic.bulder_iterator_logic import IteratorLogicBulder
from myapp.services.core_logic.bulders.bulder_iterator_id.bulder_iterator_id import IteratorIdBulder
from myapp.services.core_logic.iterator_id.iterator_id import IteratorId

class ReadyIteratorId:

    def __init__(self, maker_iterator_id:Optional[MakeIteratorId] = None ) -> None:

        if maker_iterator_id is None:
            maker_iterator_id = MakeIteratorId(
                IteratorLogicBulder,
                IteratorIdBulder
            )

        self.maker_iterator_id = maker_iterator_id
    

    @property
    def make_instance(self) -> IteratorId:
        return self.maker_iterator_id.make_ready_iterator_id()


        