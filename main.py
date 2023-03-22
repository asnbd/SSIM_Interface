import tkinter as tk
import tkinter.messagebox
import customtkinter as ctk
from tkinterdnd2 import TkinterDnD, DND_FILES

ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(ctk.CTk, TkinterDnD.DnDWrapper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.TkdndVersion = TkinterDnD._require(self)

        # configure window
        self.title("SSIM Interface")
        self.geometry(f"{1100}x{580}")

        # configure grid layout

if __name__ == "__main__":
    app = App()
    app.mainloop()
