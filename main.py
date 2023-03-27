import tkinter as tk
import tkinter.messagebox
import customtkinter as ctk
from tkinterdnd2 import TkinterDnD, DND_FILES
from PIL import ImageTk, Image

APPEARANCE_MODE = "Light"  # "System", "Dark", "Light"
DEFAULT_COLOR_THEME = "blue"  # "blue", "green", "dark-blue"

ctk.set_appearance_mode(APPEARANCE_MODE)
ctk.set_default_color_theme("blue")


class App(ctk.CTk, TkinterDnD.DnDWrapper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.TkdndVersion = TkinterDnD._require(self)

        # configure window
        self.title("SSIM Interface")
        self.geometry(f"{1100}x{580}")
        self.minsize(1100, 580)

        # configure grid layout
        self.grid_columnconfigure(1, weight=0)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = ctk.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.create_sidebar_widgets(self.sidebar_frame)

        # set default values
        self.set_default_values()

        self.create_ssim_cutcurve_frame()
        self.create_gbp_outputs_frame()

    def create_sidebar_widgets(self, frame):
        # Sidebar Logo & Title
        self.logo_label = ctk.CTkLabel(
            frame, text="SSIM Interface", font=ctk.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        # Upload Trained Model Option
        self.open_trained_model_btn = ctk.CTkButton(
            frame, command=self.open_trained_model_btn_event, text="Upload Trained Model")
        self.open_trained_model_btn.grid(row=1, column=0, padx=20, pady=10)

        # Upload Image option
        self.open_image_btn = ctk.CTkButton(
            frame, command=self.open_image_btn_event, text="Upload Image")
        self.open_image_btn.grid(row=2, column=0, padx=20, pady=10)

        # Name of convolution layers button
        self.conv_layers_entry = ctk.CTkEntry(
            frame, placeholder_text="Name of Convolution Layers")
        self.conv_layers_entry.grid(row=3, column=0, padx=20, pady=10)

        # Generate button
        self.generate_button = ctk.CTkButton(
            frame, command=self.generate_btn_event, text="Generate")
        self.generate_button.grid(row=4, column=0, padx=20, pady=10)

        # Vertical Empty Space
        frame.grid_rowconfigure(5, weight=1)

        # Appearance Mode
        self.appearance_mode_label = ctk.CTkLabel(
            frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=6, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = ctk.CTkOptionMenu(frame, values=["Light", "Dark", "System"],
                                                             command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(
            row=7, column=0, padx=20, pady=(10, 20))

    # Set Default Values
    def set_default_values(self):
        self.appearance_mode_optionemenu.set(APPEARANCE_MODE)

    # Create SSIM Cut Curve Frame
    def create_ssim_cutcurve_frame(self):
        self.ssim_cutcurve_frame = ctk.CTkScrollableFrame(
            self, label_text="SSIM Cut Curve", orientation="horizontal")
        self.ssim_cutcurve_frame.grid(
            row=0, column=2, padx=10, pady=10, sticky="nsew")

    # Create GBP Outputs Frame
    def create_gbp_outputs_frame(self):
        self.gbp_outputs_frame = ctk.CTkScrollableFrame(
            self, label_text="GBP Outputs", orientation="horizontal")
        self.gbp_outputs_frame.grid(
            row=1, column=2, padx=10, pady=10, sticky="nsew")

        self.sample_img = Image.open("images/sample_output_1.png")
        self.sample_img = self.sample_img.resize((180, 180), Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(self.sample_img)

        self.scrollable_frame_images = []
        for i in range(20):
            label = tkinter.Label(self.gbp_outputs_frame, image=self.img)
            label.grid(row=0, column=i, padx=5, pady=10)

            self.scrollable_frame_images.append(label)

    # Sidebar Events
    def open_trained_model_btn_event(self):
        # TODO: Implement Upload Trained Model Button Click Event
        pass

    def open_image_btn_event(self):
        # TODO: Implement Upload Image Button Click Event
        pass

    def generate_btn_event(self):
        # TODO: Implement Generate Button Click Event
        pass

    # Others
    def change_appearance_mode_event(self, new_appearance_mode: str):
        ctk.set_appearance_mode(new_appearance_mode)


if __name__ == "__main__":
    app = App()
    app.mainloop()
