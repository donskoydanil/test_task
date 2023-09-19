import pathlib
from typing import Type
from pydantic import BaseModel, computed_field
from myapp.services.core_logic.giver_id.giver_id import GiverId
from myapp.services.core_logic.iterator_id.iterator_id import IteratorId
from myapp.services.core_logic.iterator_id.iteration_logic.logic import IteratorLogic

class GiveIdInterface(BaseModel):
    giver_id : Type[GiverId] = GiverId(
        IteratorId(
            IteratorLogic()
            )
        )
    
    @computed_field(return_type=Type[GiverId])
    @property
    def get_ready_instance(self):
        return self.giver_id
    


def get_ready_giver_id(
        interface_maker:Type[GiveIdInterface] = GiveIdInterface()
) -> Type[GiverId]:
    interface = interface_maker.get_ready_instance
    return interface

    