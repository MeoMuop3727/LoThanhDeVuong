import pygame
from typing import Optional

class ManagerScene:
    def __init__(self,
                 size: tuple[int, int] = (1280, 920),
                 caption: str = "My Game - Debugger",
                 icon: Optional[str] = None):
        
        self.__screen = pygame.display.set_mode(size, pygame.SRCALPHA)
        pygame.display.set_caption(caption)
        pygame.display.set_icon(pygame.image.load(icon))

        # Game configs
        self.running = True
        self.fps = 60

        self.__clock = pygame.Clock()

        # STACK scenes
        self.__scenes: list["Scene"] = []
    
    def push_scene(self, scene: "Scene"):
        self.__scenes.append(scene)
        scene.on_enter()

    def pop_scene(self):
        scene = self.__scenes.pop()
        scene.on_exit()

    def replace_scene(self, scene: "Scene"):
        self.pop_scene()
        self.push_scene(scene) 

    def run_game(self):
        while self.running:
            self.__screen.fill("#ffffff")

            dt = self.__clock.tick(self.fps) / 1e3

            current_scene = self.__scenes[0] if self.__scenes else None

            if current_scene is None: continue

            for event in pygame.event.get():
                current_scene.event(event)

                if event.type == pygame.QUIT:
                    self.running = False

            current_scene.update(dt)

            pygame.display.flip()
