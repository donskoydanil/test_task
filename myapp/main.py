from aiohttp import web
from myapp.setup.setup_routes import setup_project_routes
from myapp.setup.setup_shutdown import close_app


def setup_app(application):
    setup_project_routes(application)
    application.on_shutdown.append(close_app)
    print('appication ready to work')
    

app = web.Application()


if __name__ == '__main__':
    setup_app(app)
    web.run_app(app)


