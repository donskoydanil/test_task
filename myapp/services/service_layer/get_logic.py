from typing import Callable



class ServiceGet:


    def __init__(self, maker_info_of_file:Callable[[str],str]) -> None:
        self.maker_info_of_file = maker_info_of_file

    async def start_service(self, id:str)->str:
        logic_out = self.maker_info_of_file(id)
        return logic_out
        