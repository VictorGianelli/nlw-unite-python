from typing import Dict


class HttpRequest:
    def __init__(self, body: Dict = None, param: int = None) -> None:
        self.body = body
        self.param = param