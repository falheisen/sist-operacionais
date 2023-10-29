from dataclasses import dataclass
import heapq
from inspect import isgenerator
from typing import Any, Callable, Generic, Type, TypeVar


@dataclass
class Event:
    delay: int

E = TypeVar("E", bound=Event)
C = TypeVar("C")

class Application(Generic[C]):
    
    def __init__(self, context_factory: Callable[[Any], C]) -> None:
        self._handlers: dict[Event, Callable[[E, C], Any]] = {}
        self._context_factory = context_factory

    def create_context(self, **kwargs):
        return self._context_factory(**kwargs)
    
    def handle(self, event: Event, context: C):
        return self._handlers[type(event)](event, context)
    
    def on(self, event_class: Type[E]):
        def decorator(fn: Callable[[E, C], Any]):
            if event_class in self._handlers:
                raise Exception("Handler already registered")
            self._handlers[event_class] = fn
            return fn
        return decorator
    

class Engine:

    def __init__(self, app: Application, **kwargs) -> None:
        self.time = 0
        self._app = app
        self._app_context = self._app.create_context(**kwargs)
        self._events: list[Event] = []
        
    def run(self):
        while self._events:
            time, event = self._next()
            self.time = time
            handler = self._app.handle(event, self._app_context)            
            if isgenerator(handler):
                for event in (result for result in handler if result):
                    self.schedule(event)

    def schedule(self, event: Event):
        heapq.heappush(self._events, (self.time + event.delay, len(self._events), event))

    def _next(self) -> Event:
        return heapq.heappop(self._events)