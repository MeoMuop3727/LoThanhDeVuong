import pygame
from ui import *
from scene import Scene

class Game(Scene):
    def __init__(self, manager):
        super().__init__(manager)

        self.__PADDING_TOP = 30

        self.__size_peter = (200, 2000)
        self.__pos_peter = (
            self._manager.screen.get_width() // 2 - self.__size_peter[0] // 2,
            self._manager.screen.get_height() // 2
        )
        self.__peter = pygame.Rect(self.__pos_peter, self.__size_peter)

        self.__pos_hand = (0, 0)
        self.__size_hand = (125, 300)
        self.__hand = pygame.Rect(self.__pos_hand, self.__size_hand)

        self.__score = 0.0          
        self.__level = 1
        self.__hand_prev_y = None   
        self.__touching = False

        self.__timeout = 600

        self.__SCORE_PER_LEVEL = 100

        self.__size_button_pause = (70, 70)
        self.__pos_button_pause = (
            (self._manager.screen.width - self.__size_button_pause[0]) // 2,
            self.__PADDING_TOP
        )
        self.__button_pause = Button(self._manager.screen, StyleButton(
            size=self.__size_button_pause,
            pos=self.__pos_button_pause,
            text="P",
            border_radius=15,
            font=pygame.Font("assets/font/Isometra-Regular.ttf", 25)
        ))

    def on_enter(self):
        return super().on_enter()

    def on_exit(self):
        return super().on_exit()

    def __score_needed(self, level: int) -> float:
        # Score for next level
        return self.__SCORE_PER_LEVEL * (level - 1)

    def __check_touch(self, dt):
        self.__touching = self.__peter.colliderect(self.__hand)

        if self.__touching:
            current_y = self.__hand.centery

            # The first frame collide, note pos and do not add score
            if self.__hand_prev_y is not None:
                delta = abs(current_y - self.__hand_prev_y)
                self.__score += delta * self.__score_multiplier()

            self.__hand_prev_y = current_y
        else:
            # If hand does not collide peter, minus score
            self.__hand_prev_y = None
            self.__score -= dt * (self.__level // 2)

            if self.__score <= 0:
                if self.__level <= 1:
                    self.__level = 1
                    self.__score = 0.0
                else:
                    self.__level -= 1
                    self.__score = self.__score_needed(self.__level)

    def __score_multiplier(self) -> float:
        return 1 / self.__level

    def event(self, event):
        return super().event(event)

    def update(self, dt):
        FONT = pygame.Font("assets/font/Isometra-Regular.ttf", 30)

        self.__check_touch(dt)

        mouse_pos = pygame.mouse.get_pos()
        self.__pos_hand = (
            mouse_pos[0] - self.__hand.w // 2,
            mouse_pos[1] - self.__hand.h // 2
        )
        self.__hand = pygame.Rect(self.__pos_hand, self.__size_hand)

        # Timeout
        self.__timeout -= dt
        Label(self._manager.screen, StyleLabel(
            content=f"Time: {int(self.__timeout)}",
            pos=(
                self._manager.screen.width - 115,
                self.__PADDING_TOP
            ),
            font=FONT,
            size=(0, 0)
        )).update()

        # Level
        Label(self._manager.screen, StyleLabel(
            content=f"Level: {self.__level}",
            pos=(
                95,
                self.__PADDING_TOP
            ),
            font=FONT,
            size=(0,0)
        )).update()

        score_need = self.__score_needed(self.__level)

        if self.__score > score_need:
            self.__level += 1
            self.__score = 0.0

        # Score
        Label(self._manager.screen, StyleLabel(
            content=f"{int(self.__score)}/{score_need}",
            font=FONT,
            size=(0, 0),
            pos=(
                self._manager.screen.width // 2,
                135
            )
        )).update() 

    def render(self):
        pygame.draw.rect(
            self._manager.screen,
            "red",
            self.__peter
        )

        pygame.draw.rect(
            self._manager.screen,
            "blue",
            self.__hand
        )

        self.__button_pause.update()
        self.__button_pause.press(StyleButton(
            size=self.__size_button_pause,
            pos=self.__pos_button_pause,
            border_radius=15
        ), func=lambda: self._manager.pop_scene())
