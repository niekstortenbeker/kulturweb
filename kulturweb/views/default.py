from kulturweb.viewmodels.viewmodel_default import FilterViewModel, HomeViewModel
from pyramid.request import Request
from pyramid.view import view_config


@view_config(route_name="home", renderer="kulturweb:templates/home.pt")
def home_index(request: Request):
    vm = HomeViewModel(request)
    return vm.to_dict()


@view_config(route_name="filter/", renderer="kulturweb:templates/home.pt")
@view_config(route_name="filter", renderer="kulturweb:templates/home.pt")
def filter_shows(request: Request):
    vm = FilterViewModel(request)
    return vm.to_dict()
