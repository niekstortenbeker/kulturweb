from kultur import init_fake_database
from pyramid.config import Configurator


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    with Configurator(settings=settings) as config:
        config.include("pyramid_chameleon")
        config.include(".routes")
        init_fake_database()
        config.scan()
    return config.make_wsgi_app()
