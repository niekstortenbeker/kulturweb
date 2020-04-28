from kulturweb.viewmodels.data import get_shows
from kulturweb.viewmodels.viewmodel_base import ViewModelBase
from pyramid.request import Request


class HomeViewModel(ViewModelBase):
    def __init__(self, request: Request):
        super().__init__(request)

        self.category = "alle"
        self.time_span = "heute"
        self.dubbed = "nein"
        self.shows: dict = get_shows(
            time_span="", location="", category="alle", dubbed="nein"
        )


class FilterViewModel(ViewModelBase):
    def __init__(self, request: Request):
        super().__init__(request)

        self.category = request.matchdict.get_shows("category")
        self.time_span = request.matchdict.get_shows("time_span")
        self.dubbed = request.matchdict.get_shows("dubbed")
        self.shows: dict = get_shows(
            time_span=self.time_span,
            location="",
            category=self.category,
            dubbed=self.dubbed,
        )
