from pyramid.config import Configurator


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    init_includes(config)
    init_routing(config)

    return config.make_wsgi_app()


def init_includes(config):
    config.include("pyramid_chameleon")


def init_routing(config):
    config.add_static_view("static", "static", cache_max_age=3600)

    # home controller
    config.add_route("home", "/")
    config.add_route("about", "/about")

    # filter options
    # TODO also add only /kino etc.
    # http://localhost:6543/kino/wann=heute+synchronisierter=ja
    config.add_route("filter", "/{what}/wann={when}+synchronisierter={dubbed}")
    config.add_route("filter/", "/{what}/wann={when}+synchronisierter={dubbed}/")

    config.add_route("package_details", "/project/test={package_name}")
    #               http://localhost:6543/project/awscli/releases/1.15.30
    config.scan()
