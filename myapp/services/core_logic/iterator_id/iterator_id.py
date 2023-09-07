from iteration_logic.base_logic_parts import BaseIteratorLogic


class IteratorId:

    def __init__(self,iterator_logic:BaseIteratorLogic ) -> None:
        self.iterator_logic = iterator_logic

    def __iter__(self) -> BaseIteratorLogic:
        return self.iterator_logic
        