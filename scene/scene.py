import pygame
from abc import ABC, abstractmethod
from .manager import ManagerScene

class Scene(ABC):
    def __init__(self, manager: "ManagerScene"):

        self._manager = manager

    @abstractmethod
    def on_enter(self): ...

    @abstractmethod
    def on_exit(self): ...

    @abstractmethod
    def event(self, event: pygame.Event): ...

    @abstractmethod
    def render(self): ...

    @abstractmethod
    def update(self, dt: float): ...
