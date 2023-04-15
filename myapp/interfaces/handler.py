import asyncio
from aiohttp import web
from abc import ABC, abstractmethod



class HandlerInerface(ABC):


    @abstractmethod
    async def handle(self, request:web.Request ) -> web.Response:
        pass


    