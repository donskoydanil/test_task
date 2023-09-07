from base_logic_parts import BaseIteratorLogic
from attribute_manager import AttributeManager

class IteratorLogic(BaseIteratorLogic,AttributeManager):

    def __init__(self) -> None:
        self.start_alphavite = 0
        self.start_numbers = 1
        self._make_iterator_logic_attrubutes()

    def _make_iterator_logic_attrubutes(self) -> None:
        super().make_attrubutes()

    def __next__(self) -> str:
        
        if self.start_alphavite > len(self.alphavite) - 1 :
            raise StopIteration
        
        out_line = f"{self.alphavite[self.start_alphavite]}{self.start_numbers}"
        
        if self.start_numbers == self.end_numbers:
            self.start_alphavite += 1
            self.start_numbers = 0
        
        self.start_numbers += 1

        

        return out_line
        
        