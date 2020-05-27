from kulturweb.viewmodels.viewmodel_base import ViewModelBase
from pyramid.view import notfound_view_config


@notfound_view_config(renderer="../templates/404.pt")
def notfound_view(request):
    request.response.status = 404
    vm = ViewModelBase(request)
    return vm.to_dict()
