from pyramid.view import view_config


@view_config(route_name="impressum", renderer="kulturweb:templates/impressum.pt")
def impressum(_):
    return {}


@view_config(route_name="about", renderer="kulturweb:templates/about.pt")
def about(_):
    return {}
