import asyncio
from aiohttp import web
from interfaces.handler import HandlerInerface




class StartPageHandler(HandlerInerface):


    async def handle(self, request: web.Request) -> web.Response:
        return web.Response(text='Main page')


