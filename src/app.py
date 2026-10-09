from scene import Scene, ManagerScene

class _MainScene(Scene):
    def __init__(self, manager):
        super().__init__(manager)

    def on_exit(self):
        return super().on_exit()

    def on_enter(self):
        return super().on_enter()

    def event(self, event):
        return super().event(event)

    def render(self):
        return super().render()

    def update(self, dt):
        return super().update(dt)

def App():
    manager = ManagerScene()
    main_scene = _MainScene(manager)
    manager.push_scene(_MainScene(main_scene))
    manager.run_game()
    