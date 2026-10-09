import pygame
from copy import copy
from typing import Optional, Callable
from dataclasses import dataclass

@dataclass
class StyleButton:
    size: tuple[int, int] = (100, 50)
    pos: tuple[int, int] = (0, 0)

    text: str = "click"
    font: Optional[pygame.Font] = None
    text_color: pygame.Color = "#000000"

    bg_color: pygame.Color = "#f0f0f0"

    border: int = 0
    border_radius: int = 10
    border_color: pygame.Color = "#111111"

class Button:
    def __init__(self,
                 surf: pygame.Surface,
                 style: StyleButton):

        if not isinstance(surf, pygame.Surface):
            raise TypeError
        if not isinstance(style, StyleButton):
            raise TypeError

        self.__surf = surf
        self.__style_original = style
        self.__style_modified = copy(style)

        # Rect to check collide between button and mouse
        self.__rect_mouse = pygame.Rect(self.__style_modified.pos, self.__style_modified.size)

        # Background
        self.__background = self.__rect_mouse.copy()

        # Border
        size_border = (
            self.__style_modified.size[0] + self.__style_modified.border * 2,
            self.__style_modified.size[1] + self.__style_modified.border * 2
        )
        pos_border = (
            self.__style_modified.pos[0] - self.__style_modified.border,
            self.__style_modified.pos[1] - self.__style_modified.border
        )
        self.__border = pygame.Rect(pos_border, size_border)

        # Check pressed button
        self.__pressed = False

    @property
    def pressed(self) -> bool:
        return self.__pressed

    def update(self):
        self.__drawing_border(self.__style_modified.border_color)
        self.__drawing_background(self.__style_modified.bg_color)
        self.__drawing_text(self.__style_modified.text_color, self.__style_modified.text)

    def hover(self, new_style: StyleButton):
        if not isinstance(new_style, StyleButton):
            return TypeError

        mouse_pos = pygame.mouse.get_pos()

        if self.__rect_mouse.collidepoint(mouse_pos):
            self.__style_modified = copy(new_style)
        else:
            self.__style_modified = copy(self.__style_original)

    def press(self, new_style: StyleButton, func: Optional[Callable] = None):
        if not isinstance(new_style, StyleButton): 
            return TypeError

        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()[0]

        if self.__rect_mouse.collidepoint(mouse_pos):
            if mouse_pressed:
                if not self.__pressed:
                    self.__pressed = True
                    if func is not None: func()
                self.__style_modified = copy(new_style)
            else:
                self.__pressed = False
                self.__style_modified = copy(self.__style_original)
        else:
            self.__pressed = False 
            self.__style_modified = copy(self.__style_original)

    def __drawing_border(self, color: pygame.Color):
        if self.__style_modified.border < 0: return

        pygame.draw.rect(self.__surf, color, self.__border, 0, self.__style_modified.border_radius)

    def __drawing_background(self, color: pygame.Color):
        pygame.draw.rect(self.__surf, color, self.__background, 0, self.__style_modified.border_radius)

    def __drawing_text(self, color: pygame.Color, text: str):
        if not self.__style_modified.font: return

        text_surf = self.__style_modified.font.render(text, True, color)
        text_rect = text_surf.get_rect(center=self.__background.center)
        self.__surf.blit(text_surf, text_rect)

