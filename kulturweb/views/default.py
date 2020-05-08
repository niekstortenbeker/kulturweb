from kulturweb.viewmodels.viewmodel_default import FilterViewModel, HomeViewModel
from pyramid.request import Request
from pyramid.view import view_config


@view_config(route_name="home", renderer="kulturweb:templates/home.pt")
def home(request: Request):
    vm = HomeViewModel(request)
    return vm.to_dict()


@view_config(route_name="filter/", renderer="kulturweb:templates/home.pt")
@view_config(route_name="filter", renderer="kulturweb:templates/home.pt")
def filter_shows(request: Request):
    vm = FilterViewModel(request)
    return vm.to_dict()
    # TODO maybe do try except here https://docs.pylonsproject.org/projects/pyramid/en/latest/tutorials/wiki2/basiclayout.html#view-declarations-via-the-views-package


# @view_config(route_name="location/", renderer="kulturweb:templates/home.pt")
# @view_config(route_name="location", renderer="kulturweb:templates/home.pt")
# def filter_shows(request: Request):
#     vm = LocationViewModel(request)
#     return vm.to_dict()
