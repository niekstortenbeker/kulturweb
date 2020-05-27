from typing import Dict, Union

from pyramid.request import Request


class ViewModelBase:
    def __init__(self, request: Request):
        self.request: Request = request
        self.app_url: str = request.registry.settings.get(
            "kulturweb.app_url", "http://localhost:6543/"
        )
        self.error: Union[str, None] = None

    def to_dict(self) -> Dict:
        return self.__dict__
