def includeme(config):
    config.add_static_view("static", "static", cache_max_age=3600)

    # home controller
    config.add_route("home", "/")
    config.add_route("about", "/about")
    config.add_route("impressum", "/impressum")

    # filter options
    config.add_route(
        "filter", "/{category}/{location}/wann={time_span}+synchronisierter={dubbed}"
    )
    config.add_route(
        "filter/", "/{category}/{location}/wann={time_span}+synchronisierter={dubbed}/"
    )
