import pygame
from typing import Optional
from dataclasses import dataclass
from copy import copy

@dataclass(slots=True)
class StyleLabel:
    content: str = ""
    text_color: pygame.Color = "#000000"
    font: Optional[pygame.Font] = None

    size: tuple[int, int] = (100, 100)
    pos: tuple[int, int] = (0, 0)

    bg_color: pygame.Color = "#f0f0f0"

    border: int = 0
    border_color: pygame.Color = "#000000"
    border_radius: int = 0

class Label:
    def __init__(self,
                 surf: pygame.Surface,
                 style: StyleLabel):
        
        if not isinstance(surf, pygame.Surface):
            raise TypeError
        if not isinstance(style, StyleLabel):
            raise TypeError

        self.__surf = surf
        self.__style_modified = copy(style)
        self.__style_original = style

        # Background
        self.__background = pygame.Rect(self.__style_modified.pos, self.__style_modified.size)

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

    @property
    def content(self) -> str:
        return self.__style_modified.content

    def update(self):
        self.__drawing_border(self.__style_modified.border_color)
        self.__drawing_background(self.__style_modified.bg_color)
        self.__drawing_text(self.__style_modified.text_color, self.__style_modified.content)

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

