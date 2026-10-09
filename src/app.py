import pygame
from pyvidplayer2 import Video

from ui import *
from scene import Scene, ManagerScene
from utils.config import load_game

from .scenes import *

# Theme music
pygame.mixer.music.load("assets/audio/Aaron Smith - Dancin (KRONO Remix).mp3")
pygame.mixer.music.set_volume(1.0)
pygame.mixer.music.play(loops=-1, fade_ms=2000)

FONT_GAME = "assets/font/Isometra-Regular.ttf"
DATA_GAME = "data/savegame.json"
class _MainScene(Scene):
    def __init__(self, manager):
        super().__init__(manager)

        self.__screen = self._manager.screen

        self.__caption_game = Label(self.__screen, StyleLabel(
            content="LoThanhDeVuong",
            font=pygame.Font(FONT_GAME, 45),
            size=(0,0),
            pos=(self.__screen.get_width() // 2, 70)
        ))

        self.__size_button = (400, 100)
        self.__button_play = Button(self.__screen, StyleButton(
            size=self.__size_button,
            pos=(self.__screen.get_width() // 2 - self.__size_button[0] // 2, 550),
            text="LamQuaLo",
            font=pygame.Font(FONT_GAME, 35)
        ))
        self.__button_settings = Button(self.__screen, StyleButton(
            size=self.__size_button,
            pos=(self.__screen.get_width() // 2 - self.__size_button[0] // 2, 550 + self.__size_button[1] + 20),
            text="Setting",
            font=pygame.Font(FONT_GAME, 35)
        ))

        self.__data_game = load_game(DATA_GAME)

        self.__highest_score = Label(self.__screen, StyleLabel(
            content=f"Highest Score: {self.__data_game["game"]["score"]["max"]}",
            size=(0, 0),
            font=pygame.Font(FONT_GAME, 30),
            pos=(
                self.__screen.width // 2,
                250
            )
        ))

        self.__current_score = Label(self.__screen, StyleLabel(
            content=f"Current Score: {self.__data_game["game"]["score"]["current"]}",
            size=(0, 0),
            font=pygame.Font(FONT_GAME, 30),
            pos=(
                self.__screen.width // 2,
                335
            )
        ))

        self.__POEMS = [
            "Dem thau tinh mich thanh van,",
            "Nhat thoi vong niem xoay van chenh venh.",
            "Hu khong sac tuong mong menh,",
            "Tam hon lang le, bong benh tich lieu.",
            "Hoi long chap niem bao nhieu,",
            "Sac khong huyen mong, som chieu doi thay.",
            "Chi bang tinh toa hom nay,",
            "Quan tam tu tai, to ngay thanh tan.",
        ]

    def on_exit(self):
        return super().on_exit()

    def on_enter(self):
        return super().on_enter()

    def event(self, event):
        return super().event(event)

    def __change_scene_game(self):
        click = pygame.mixer.Sound("assets/audio/an_ba_to_com_ban_goc-www_tiengdong_com.mp3")
        click.set_volume(1.0)
        pygame.mixer.music.set_volume(0.4)
        click.play(fade_ms=1000)

        self._manager.replace_scene(Loadding(self._manager))
        pygame.mixer.music.set_volume(1.0)

    def render(self):
        # Caption
        self.__caption_game.update()

        # Score
        self.__highest_score.update()
        self.__current_score.update()

        # Poem
        GAP_POEM = 35
        for idx, poem in enumerate(self.__POEMS):
            Label(self.__screen, StyleLabel(
                content=poem,
                font=pygame.Font(FONT_GAME, 20),
                size=(0,0),
                pos=(
                    self.__screen.width // 2,
                    960 + GAP_POEM * idx
                )
            )).update()

        # Playing button
        self.__button_play.update()
        self.__button_play.press(
            StyleButton(
                size=self.__size_button,
                pos=(self.__screen.get_width() // 2 - self.__size_button[0] // 2, 700),
                text="LamQuaLo",
                font=pygame.Font(FONT_GAME, 35),
                text_color="#f0f0f0"
            ),
            func=lambda: self.__change_scene_game()
        )

        # Setting button
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
    