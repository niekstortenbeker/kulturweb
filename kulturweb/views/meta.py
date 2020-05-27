from kulturweb.viewmodels.viewmodel_base import ViewModelBase
from pyramid.view import view_config


@view_config(route_name="impressum", renderer="kulturweb:templates/impressum.pt")
def impressum(request):
    vm = ViewModelBase(request)
    return vm.to_dict()


@view_config(route_name="about", renderer="kulturweb:templates/about.pt")
def about(request):
    vm = ViewModelBase(request)
    return vm.to_dict()
