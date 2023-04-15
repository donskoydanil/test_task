
from aiohttp import web 
from settings import routes



def setup_project_routes(app):
    app.add_routes(routes)
