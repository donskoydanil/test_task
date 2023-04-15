from aiohttp import web
from setup.setup_routes import setup_project_routes


def setup_app(application):

    setup_project_routes(application)
    print('appication ready to work')



app = web.Application()


if __name__ == '__main__':
    setup_app(app)
    web.run_app(app)


