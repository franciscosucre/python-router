# Standard libs imports
import re
import typing
from typing import List, Pattern, Callable, Dict, Union, NewType, TypeVar

Method = Union['GET', 'POST']

RouteIndex = Dict[Method, List[Callable]]

class Route:
    url_pattern: str
    handlers: typing.Callable
    regex: Pattern
    index: RouteIndex

    def __init__(self: 'Route', method: Method, url_pattern: str, first_handler: Callable,  *handlers: List[Callable]):
        self.url_pattern = url_pattern
        self.regex = re.compile(url_pattern)
        route_handlers = [first_handler]
        for handler in handlers:
            route_handlers.append(handler)
        self.index.update(method, handlers)
        self.handlers = [first_handler]
        if len(handlers) > 0:
            self.handlers = self.handlers + handlers


class Router:
    routes: Dict[str, Route] = dict()
    routes: typing.List[Route] = list()

    def add_route(self: 'Router', method: Method, url_pattern: str, first_handler: Callable,  *handlers: List[Callable]):
        route = Route(url_pattern, method, first_handler,  *handlers)
        self.routes[url_pattern] = Route

    def find(self, url: str):
        patterns = [r.regex for r in self.routes.values()]
        for pattern in patterns:
            if pattern.match(url):
                return pattern


