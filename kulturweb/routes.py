def includeme(config):
    config.add_static_view("static", "static", cache_max_age=3600)

    # home controller
    config.add_route("home", "/")
    config.add_route("about", "/about")

    # filter options
    # TODO also add only /kino etc.
    # http://localhost:6543/kino/schauburg/wann=heute+synchronisierter=ja
    # config.add_route("filter", "/{category}/wann={time_span}+synchronisierter={dubbed}")
    # config.add_route(
    #     "filter/", "/{category}/wann={time_span}+synchronisierter={dubbed}/"
    # )
    config.add_route(
        "filter", "/{category}/{location}/wann={time_span}+synchronisierter={dubbed}"
    )
    config.add_route(
        "filter/", "/{category}/{location}/wann={time_span}+synchronisierter={dubbed}/"
    )

    # # with location
    # # http://localhost:6543/kino/schauburg/wann=heute+synchronisierter=ja
    # config.add_route("location",
    #                  "/{category}/{location}/wann={time_span}+synchronisierter={dubbed}"
    #                  )
    # config.add_route("location/",
    #                  "/{category}/{location}/wann={time_span}+synchronisierter={dubbed}/"
    #                  )
