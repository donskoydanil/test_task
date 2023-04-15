from aiohttp import web
from handlers.starthandler import StartPageHandler
from functools import partial

start_handler = StartPageHandler()
routes = [
    web.get('/',partial(start_handler.handle))

]



