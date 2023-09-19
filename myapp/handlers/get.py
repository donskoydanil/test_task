import aiohttp
from aiohttp import web
from typing import Type
from myapp.services.service_layer.get_logic import ServiceGet


class GetHandler:
    
    def __init__(self, get_logic:Type[ServiceGet]) -> None:
        self.get_logic = get_logic

    async def handler_reaction(self, request: aiohttp.ClientResponse):
        file_id = request.match_info.get('id')
        handler_out = await self.get_logic.start_service(file_id)
        return web.Response(text=handler_out)