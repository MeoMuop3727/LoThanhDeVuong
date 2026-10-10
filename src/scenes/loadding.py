import pygame
from scene import Scene
from .game import Game
from ui import Label, StyleLabel

from utils.paths import *

class Loadding(Scene):
    def __init__(self, manager):
        super().__init__(manager)

        self.__time_loadding = 5.67

        self.__elapsed = 0.0

        self.__load_text = "Loadding"
        self.__dot_interval = 400
        self.__max_dots = 3
        self.__last_tick = pygame.time.get_ticks()
        self.__dots = 0

    def on_exit(self):
        return super().on_exit()

    def on_enter(self):
        return super().on_enter()

    def event(self, event):
        return super().event(event)

    def render(self):
        self._manager.screen.fill("#000000")

        Label(self._manager.screen, StyleLabel(
            content=self.__load_text,
            font=pygame.Font(resource_path("assets/font/Isometra-Regular.ttf"), 30),
            pos=(
                self._manager.screen.width - 115,
                self._manager.screen.height - 50
            ),
            text_color="#ffffff",
            size=(0,0)
        )).update()

    def update(self, dt):
        now = pygame.time.get_ticks()
        if now - self.__last_tick >= self.__dot_interval:
            self.__last_tick = now
            self.__dots = (self.__dots + 1) % (self.__max_dots + 1)
            self.__load_text = "Loadding" + "." * self.__dots

        self.__elapsed += dt
        if self.__elapsed >= self.__time_loadding:
            self._manager.replace_scene(Game(self._manager))
    

