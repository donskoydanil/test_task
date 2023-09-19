from aiohttp import web
from myapp.setup.setup_handlers import get_ready_post_handler
from myapp.setup.setup_handlers import get_ready_get_handler





def setup_project_routes(app):

    post_handler = get_ready_post_handler()
    get_handler = get_ready_get_handler()

    app.add_routes([
        web.post('/POST/{archive}', post_handler.handler_reaction),
        web.get('/GET/{id}', get_handler.handler_reaction)
    ])
