from myapp.services.core_logic.bulders.bulder_interface.base_bulder import BaseBulder
from myapp.services.core_logic.iterator_logic.iterator_logic import IteratorLogic
from myapp.services.core_logic.iterator_logic.iterator_logic_interface import BaseIteratorLogic

class IteratorLogicBulder(BaseBulder):

    @property
    def ready_instanse(self) -> BaseIteratorLogic:
        return IteratorLogic()
        