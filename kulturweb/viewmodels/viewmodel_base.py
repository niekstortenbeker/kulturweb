from typing import Union

from pyramid.request import Request


class ViewModelBase:
    def __init__(self, request: Request):
        self.request = request
        self.error: Union[str, None] = None

    def to_dict(self):
        return self.__dict__
