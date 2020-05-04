from typing import Dict, Union

from pyramid.request import Request


class ViewModelBase:
    def __init__(self, request: Request):
        self.request: Request = request
        self.error: Union[str, None] = None

    def to_dict(self) -> Dict:
        return self.__dict__
