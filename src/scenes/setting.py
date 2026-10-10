import pygame
import customtkinter as ctk
import multiprocessing as mp
from scene import Scene
from ui import *

FONT_GAME = "assets/font/Isometra-Regular.ttf"
CONTENT = {
    "About us": [
        ("Who we are",
         "We are [Your name / Team name], a small group of developers who love "
         "making simple, funny and slightly absurd games. This project started as "
         "an experiment with Pygame and grew into something we are proud to share."),
        ("Our goal",
         "To build small games that are quick to pick up, easy to laugh at, and "
         "fun to beat your own high score in."),
        ("Contact",
         "Email: []\n"
         "GitHub: [https://github.com/MeoMuop3727]"),
    ],

    "How to play": [
        ("Controls",
         "Move your mouse to control the hand. The hand follows your cursor, so "
         "there is nothing to memorize. Press the P button at the top to pause "
         "and return to the main menu."),
        ("Scoring",
         "Keep the hand on the target and move it up and down. The faster and "
         "farther you move, the more points you earn."),
        ("Don't stop!",
         "If the hand stays still or leaves the target, your score slowly drains. "
         "Keep the rhythm going."),
        ("Levels",
         "Fill the score bar to reach the next level. Every level asks for more "
         "points, and each movement is worth a little less, so the game gets "
         "harder as you climb. Fall too low and you drop back a level."),
        ("Time limit",
         "You have a limited amount of time per run. Reach the highest level you "
         "can before the timer hits zero."),
        ("Saving",
         "Your current score and your highest score are saved automatically when "
         "you pause or when time runs out."),
    ],

    "Intro": [
        ("Welcome",
         "Welcome to [Game title]! A tiny arcade challenge about rhythm, "
         "stamina and focus."),
        ("The story",
         "Peter has a very important job for you, and he is not going to wait. "
         "Keep up the pace, keep your cool, and see how far you can go before "
         "time runs out."),
        ("Version",
         "v1.5.0-beta (Early Access). This is an early build, so you may run "
         "into bugs and missing features. Thank you for playing and for your "
         "patience!"),
        ("Humor notice",
         "This game contains light, cheeky humor intended for adult players."),
    ],

    "Assets used": [
        ("Fonts",
         "Isometra-Regular - [Ben Dunkle / https://fonts.google.com/specimen/Isometra?preview.script=Latn / license]"),
        ("Music",
         "[Track title] by [Artist] - [source link / license]\n"
         "Please make sure you have the right to distribute any music included "
         "in your release."),
        ("Images",
         "peter.png - [author / source link / license]\n"
         "hand.png - [author / source link / license]"),
        ("Libraries",
         "Pygame - https://www.pygame.org (LGPL)\n"
         "CustomTkinter - https://github.com/TomSchimansky/CustomTkinter (MIT)"),
        ("Ownership",
         "All third-party assets belong to their respective owners and are "
         "credited here. If you believe something is missing or credited "
         "incorrectly, please contact us and we will fix it."),
    ],

    "Term": [
        ("Use of the game",
         "This game is provided for entertainment purposes only. By playing, "
         "you agree to these terms."),
        ("No warranty",
         "The game is an early access build provided \"as is\", without warranty "
         "of any kind. We are not responsible for bugs, crashes or lost save data."),
        ("Your data",
         "The game only stores your name, birthday, scores and achievements "
         "locally on your device, in the save file. We do not collect or send "
         "any personal data anywhere."),
        ("Third-party content",
         "Fonts, music and images belong to their respective owners (see "
         "\"Assets used\"). Do not extract or redistribute them separately "
         "without permission from the original authors."),
        ("Changes",
         "These terms may change in future versions of the game."),
    ],
}

class Setting(Scene):
    def __init__(self, manager):
        super().__init__(manager)

        self.__button_exit = Button(self._manager.screen, StyleButton(
            size=(50,50),
            text="X",
            border_radius=10,
            pos=(10,10),
            font=pygame.Font(None, 35)
        ))

        self.__buttons = {
            "About us": None,
            "How to play": None,
            "Intro": None,
            "Assets used": None,
            "Term": None
        }
        self.__list_buttons: list[Button] = []
        self.__list_labels: list[Label] = []

        self.__current: mp.Process | None = None

    def __show_info_win(self, title: str):
        sections = CONTENT.get(title)
        if sections is None:
            return

        family = "Isometra"

        win = ctk.CTk()
        win.title(title)
        win.resizable(False, False)

        # Center on the screen; automatically reduce height if the screen is shorter than 1000px
        w, h = (620, 1000)
        h = min(h, win.winfo_screenheight() - 80)
        x = (win.winfo_screenwidth() - w) // 2
        y = max(0, (win.winfo_screenheight() - h) // 2 - 20)
        win.geometry(f"{w}x{h}+{x}+{y}")

        font_title = ctk.CTkFont(family=family, size=30, weight="bold")
        font_head = ctk.CTkFont(family=family, size=19, weight="bold")
        font_body = ctk.CTkFont(family=family, size=15)
        font_btn = ctk.CTkFont(family=family, size=16, weight="bold")

        ctk.CTkLabel(win, text=title, font=font_title).pack(pady=(25, 10))

        # Sliderbar
        frame = ctk.CTkScrollableFrame(win, corner_radius=12, fg_color="#f2f2f2")
        frame.pack(fill="both", expand=True, padx=20, pady=(5, 10))

        for head, body in sections:
            ctk.CTkLabel(frame, text=head, font=font_head, anchor="w",
                        justify="left").pack(fill="x", padx=15, pady=(15, 2))
            ctk.CTkLabel(frame, text=body, font=font_body, anchor="w",
                        justify="left", wraplength=500).pack(fill="x", padx=15, pady=(0, 5))

        ctk.CTkButton(win, text="Close", font=font_btn, width=140, height=40,
                    corner_radius=10, command=win.destroy).pack(pady=(5, 20))

        win.mainloop()  

    def __is_info_open(self) -> bool:
        return self.__current is not None and self.__current.is_alive()

    def __open_infor_window(self, title: str):
        if self.__is_info_open(): return 

        self.__current = mp.Process(target=self.__show_info_win, args=(title,), daemon=True)
        self.__current.start()

    def on_enter(self):
        size_button = (80, 80)
        GAP = 25
        for idx, (key, _) in enumerate(self.__buttons.items()):
            self.__list_buttons.append(Button(self._manager.screen, StyleButton(
                size=size_button,
                text=f"{key[0]}",
                font=pygame.Font(FONT_GAME, 35),
                border_radius=15,
                pos=(
                    10,
                    100 + (size_button[0] + GAP) * idx
                )
            )))

            self.__list_labels.append(Label(self._manager.screen, StyleLabel(
                content=key,
                font=pygame.Font(FONT_GAME, 25),
                size=(0,0),
                pos=(
                    120 + size_button[0] + GAP,
                    135 + (size_button[0] + GAP) * idx
                )
            )))

    def on_exit(self):
        return super().on_exit()

    def event(self, event):
        return super().event(event)

    def render(self):
        blocked = self.__is_info_open()

        self.__button_exit.update()
        if not blocked:
            self.__button_exit.press(StyleButton(
                pos=(50,50)
            ), lambda: self._manager.pop_scene())

        for btn in self.__list_buttons:
            btn.update()

        for idx, label in enumerate(self.__list_labels):
            label.update()
            if not blocked:
                self.__list_buttons[idx].press(StyleButton(
                    pos=self.__list_buttons[idx].pos
                ), lambda: self.__open_infor_window(label.content))

    def update(self, dt):
        if self.__is_info_open(): return 
        return super().update(dt)

