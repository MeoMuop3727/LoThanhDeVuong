import pygame
from ui import *
from scene import Scene, ManagerScene

FONT_GAME = "assets/font/Isometra-Regular.ttf"
class _MainScene(Scene):
    def __init__(self, manager):
        super().__init__(manager)

        self.__screen = self._manager.screen

        self.__caption_game = Label(self.__screen, StyleLabel(
            content="LoThanhDeVuong",
            text_color="#111111",
            font=pygame.Font(FONT_GAME, 45),
            bg_color="#ffffff",
            pos=(self.__screen.get_width() // 2 - 50, 100)
        ))

        self.__size_button = (400, 100)
        self.__button_play = Button(self.__screen, StyleButton(
            size=self.__size_button,
            pos=(self.__screen.get_width() // 2 - self.__size_button[0] // 2, 700),
            text="LamQuaLo",
            font=pygame.Font(FONT_GAME, 35)
        ))
        self.__button_settings = Button(self.__screen, StyleButton(
            size=self.__size_button,
            pos=(self.__screen.get_width() // 2 - self.__size_button[0] // 2, 700 + self.__size_button[1] + 20),
            text="Setting",
            font=pygame.Font(FONT_GAME, 35)
        ))

    def on_exit(self):
        return super().on_exit()

    def on_enter(self):
        return super().on_enter()

    def event(self, event):
        return super().event(event)

    def render(self):
        self.__caption_game.update()

        self.__button_play.update()
        self.__button_play.press(
            StyleButton(
                size=self.__size_button,
                pos=(self.__screen.get_width() // 2 - self.__size_button[0] // 2, 700),
                text="LamQuaLo",
                font=pygame.Font(FONT_GAME, 35),
                text_color="#f0f0f0"
            )
        )

        self.__button_settings.update()
        self.__button_settings.press(
            StyleButton(
                size=self.__size_button,
                pos=(self.__screen.get_width() // 2 - self.__size_button[0] // 2, 700),
                text="Setting",
                font=pygame.Font(FONT_GAME, 35),
                text_color="#f0f0f0"
            )
        )

    def update(self, dt):
        return super().update(dt)

def App():
    manager = ManagerScene(
        size=(720, 1280)
    )
    main_scene = _MainScene(manager)
    manager.push_scene(main_scene)
    manager.run_game()
    