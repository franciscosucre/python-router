# Standard libs imports
import re
import typing
from typing import List, Pattern, Callable, Dict, Union, NewType, TypeVar, Tuple

Method = Union['GET', 'POST']

RouteIndex = Dict[Method, List[Callable]]

Handler = Callable

class Route:
    url_pattern: str
    handlers: typing.Callable
    regex: Pattern
    index: RouteIndex = dict()

    def __init__(self: 'Route', method: Method, url_pattern: str, first_handler: Handler,  *handlers: Tuple[Handler]):
        self.url_pattern = url_pattern
        self.regex = re.compile(url_pattern)
        route_handlers = [first_handler]
        for handler in handlers:
            route_handlers.append(handler)
        self.index.update({method: handlers})
        self.handlers = [first_handler]
        if len(handlers) > 0:
            self.handlers = self.handlers + list(handlers)


class Router:
    routes: Dict[str, Route] = dict()

    def add_route(self: 'Router', method: Method, url_pattern: str, first_handler: Handler,  *handlers: Tuple[Handler]):
        route = Route(method,url_pattern, first_handler,  *handlers)
        self.routes.update({url_pattern: route})

    def get(self, url_pattern: str, first_handler: Handler,  *handlers: Tuple[Handler]):
        self.add_route('GET',  url_pattern, first_handler,  *handlers)

    def find_route(self, url: str):
        routes = [i[1] for i in self.routes.items()]
        for route in routes:
            if route.regex.match(url):
                return route



