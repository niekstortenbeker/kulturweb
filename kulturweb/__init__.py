from kultur import init_database
from pyramid.config import Configurator

__version__ = "0.1"
__author__ = "Niek Stortenbeker"


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    with Configurator(settings=settings) as config:
        config.include("pyramid_chameleon")
        config.include(".routes")
        init_database()
        config.scan()
    return config.make_wsgi_app()
