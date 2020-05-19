from typing import Dict, List

from kulturweb.viewmodels.data import shows
from kulturweb.viewmodels.data.timespans import get_time_span_options
from kulturweb.viewmodels.viewmodel_base import ViewModelBase
from pyramid.request import Request


class HomeViewModel(ViewModelBase):
    def __init__(self, request: Request):
        super().__init__(request)

        self.category: str = "alle"
        self.time_span: str = "heute"
        self.dubbed: str = "nein"
        self.location: str = "alle"
        self.time_span_options: Dict = get_time_span_options(self.time_span)
        self.shows: List = shows.get_shows(
            time_span=self.time_span,
            category=self.category,
            dubbed=self.dubbed,
            location=self.location,
        )


class FilterViewModel(ViewModelBase):
    def __init__(self, request: Request):
        super().__init__(request)

        self.category: str = request.matchdict.get("category")
        self.time_span: str = request.matchdict.get("time_span")
        self.dubbed: str = request.matchdict.get("dubbed")
        self.location: str = request.matchdict.get("location")
        self.time_span_options: Dict = get_time_span_options(self.time_span)
        self.shows: List = []

    def validate(self):
        if self.category not in shows.valid_categories:
            self.error = "not a valid url"
            return
        if self.time_span not in shows.valid_time_spans:
            self.error = "not a valid url"
            return
        if self.dubbed not in shows.valid_dubbed:
            self.error = "not a valid url"
            return
        if self.location not in shows.valid_locations:
            self.error = "not a valid url"
            return

    def set_shows(self):
        self.shows: List = shows.get_shows(
            time_span=self.time_span,
            category=self.category,
            dubbed=self.dubbed,
            location=self.location,
        )
