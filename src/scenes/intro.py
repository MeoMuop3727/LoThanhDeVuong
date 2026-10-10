import pygame
from scene import Scene
from ui import Label, StyleLabel

from utils.paths import *
class Intro(Scene):
    def __init__(self, manager):
        super().__init__(manager)

        self.__loading_time = 3
        self.__elapsed = 0.0

        self.__caption1 = "Make by"
        self.__label_c1 = Label(self._manager.screen, StyleLabel(
            content=self.__caption1,
            size=(0, 0),
            pos=(
                self._manager.screen.width // 2 - 205,
                self._manager.screen.height // 2 - 50
            ),
            font=pygame.Font(resource_path("assets/font/Isometra-Regular.ttf"), 25),
            text_color="#ffffff"
        ))

        self.__caption2 = "OnePlay Studio"
        self.__label_c2 = Label(self._manager.screen, StyleLabel(
            content=self.__caption2,
            size=(0, 0),
            pos=(
                self._manager.screen.width // 2,
                self._manager.screen.height // 2
            ),
            font=pygame.Font(resource_path("assets/font/Isometra-Regular.ttf"), 55),
            text_color="#ffffff"
        ))

        self.__version = "v1.4.0"
        self.__label_version = Label(self._manager.screen, StyleLabel(
            content=self.__version,
            size=(0, 0),
            pos=(
                self._manager.screen.width - 45,
                self._manager.screen.height - 20
            ),
            font=pygame.Font(resource_path("assets/font/Isometra-Regular.ttf"), 15),
            text_color="#ffffff"
        ))

    def on_enter(self):
        return super().on_enter()

    def on_exit(self):
        return super().on_exit()

    def event(self, event):
        return super().event(event)

    def render(self):
        self._manager.screen.fill("#000000")

        self.__label_c1.update()
        self.__label_c2.update()
        self.__label_version.update()

    def update(self, dt):
        from ..app import _MainScene

        self.__elapsed += dt

        if self.__elapsed >= self.__loading_time:
            self._manager.replace_scene(_MainScene(self._manager))

