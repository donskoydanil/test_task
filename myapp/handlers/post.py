import aiohttp
from aiohttp import web
from typing import Type
from myapp.services.service_layer.post_logic import ServicePost


class PostHandler:

    def __init__(self, post_logic: Type[ServicePost]) -> None:
        self.post_logic = post_logic


    async def handler_reaction(self, request: aiohttp.ClientResponse):
        file_name = request.match_info.get('archive')
        id_out = await self.post_logic.start_service(file_name)
        return web.Response(text=id_out)
        
 
        



