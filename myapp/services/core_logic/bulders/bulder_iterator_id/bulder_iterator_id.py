from myapp.services.core_logic.bulders.bulder_interface.base_bulder import BaseBulder
from myapp.services.core_logic.iterator_logic.iterator_logic_interface import BaseIteratorLogic
from myapp.services.core_logic.iterator_id.iterator_id import IteratorId


class IteratorIdBulder(BaseBulder):

    def __init__(self, ready_iterator_logic:BaseIteratorLogic) -> None:
        self.ready_iterator_logic = ready_iterator_logic

    @property
    def ready_instanse(self) -> IteratorId:
        return IteratorId(self.ready_iterator_logic)
        