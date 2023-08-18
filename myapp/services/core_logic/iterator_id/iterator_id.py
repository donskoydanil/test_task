from myapp.services.core_logic.iterator_logic.iterator_logic_interface import BaseIteratorLogic


class IteratorId:

    def __init__(self,iterator_logic:BaseIteratorLogic ) -> None:
        self.iterator_logic = iterator_logic

    def __iter__(self) -> BaseIteratorLogic:
        return self.iterator_logic
        