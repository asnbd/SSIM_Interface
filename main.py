import os
import tkinter as tk
import tkinter.messagebox
import customtkinter as ctk
from tkinterdnd2 import TkinterDnD, DND_FILES
from PIL import ImageTk, Image
from tkinter import filedialog

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
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = ctk.CTkFrame(self, width=320, corner_radius=0)
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

        image_path = os.path.join(os.path.dirname(
            os.path.realpath(__file__)), "images")
        # Upload Trained Model Option
        # self.open_trained_model_btn = ctk.CTkButton(
        #     frame, width=180, command=self.open_trained_model_btn_event, text="Upload Trained Model")
        # self.open_trained_model_btn.grid(row=1, column=0, padx=20, pady=10)
        self.add_file_image = ctk.CTkImage(
            light_image=Image.open(os.path.join(
                image_path, "add-file-light.png")),
            dark_image=Image.open(os.path.join(image_path, "add-file-dark.png")), size=(32, 32))

        self.file_img = ctk.CTkImage(
            light_image=Image.open(os.path.join(
                image_path, "file.png")),
            dark_image=Image.open(os.path.join(image_path, "file.png")), size=(64, 64))

        self.add_image = ctk.CTkImage(
            light_image=Image.open(os.path.join(
                image_path, "add-image-light.png")),
            dark_image=Image.open(os.path.join(image_path, "add-image-dark.png")), size=(32, 32))

        self.open_trained_model_btn = ctk.CTkButton(
            frame, text="Upload Trained Model", image=self.add_file_image, compound="top", fg_color=("gray75", "gray25"),
            text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), width=180, height=110, command=self.open_trained_model_btn_event)
        self.open_trained_model_btn.grid(row=1, column=0, padx=20, pady=10)

        # Upload Image option
        self.open_image_btn = ctk.CTkButton(
            frame, text="Upload Image", image=self.add_image, compound="top", fg_color=("gray75", "gray25"),
            text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), width=180, height=110, command=self.open_image_btn_event)
        self.open_image_btn.grid(row=2, column=0, padx=20, pady=10)

        # Drag and Drop Register
        self.open_trained_model_btn.drop_target_register(DND_FILES)
        self.open_trained_model_btn.dnd_bind(
            "<<Drop>>", self.drop_trained_model)
        self.open_image_btn.drop_target_register(DND_FILES)
        self.open_image_btn.dnd_bind("<<Drop>>", self.drop_image)

        # Name of convolution layers button
        self.conv_layers_entry = ctk.CTkEntry(
            frame, width=180, placeholder_text="Name of Convolution Layers")
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
            row=0, column=1, padx=10, pady=10, sticky="nsew")

    # Create GBP Outputs Frame
    def create_gbp_outputs_frame(self):
        self.gbp_outputs_frame = ctk.CTkScrollableFrame(
            self, label_text="GBP Outputs", orientation="horizontal")
        self.gbp_outputs_frame.grid(
            row=1, column=1, padx=10, pady=10, sticky="nsew")

        self.sample_img = Image.open("images/sample_output_1.png")
        self.sample_img = self.sample_img.resize(
            (180, 180), Image.Resampling.LANCZOS)
        self.img = ImageTk.PhotoImage(self.sample_img)

        self.scrollable_frame_images = []
        for i in range(20):
            label = tkinter.Label(self.gbp_outputs_frame, image=self.img)
            label.grid(row=0, column=i, padx=5, pady=10)

            self.scrollable_frame_images.append(label)

    # File Browser
    def open_file(self, type=0):
        file_types = [
            (("H5 Model", "*.h5"), ("All files", "*.*")),
            (("PNG Images", "*.png"), ("JPG Images", "*.jpg"))
        ]

        title = "Select File" if type == 0 else "Select Image"

        filename = filedialog.askopenfilename(
            title=title, filetypes=file_types[type])

        return filename

    # Sidebar Events
    def open_trained_model_btn_event(self):
        # TODO: Update Upload Trained Model Button Click Event
        file_path = self.open_file()
        if file_path:
            self.preview_file(file_path)

    def open_image_btn_event(self):
        # TODO: Update Upload Image Button Click Event
        file_path = self.open_file(1)
        if file_path:
            self.preview_image(file_path)

    def preview_file(self, file_path):
        filename = os.path.basename(file_path)
        self.open_trained_model_btn.configure(image=self.file_img)
        self.open_trained_model_btn.configure(
            text=self.get_truncated_file_name(filename) + "\nModel File")

    def preview_image(self, file_path):
        filename = os.path.basename(file_path)
        # TODO: Fix to support HighDPI
        # self.open_img = ctk.CTkImage(Image.open(file_path), size=(64, 64))
        img = Image.open(file_path)
        img.thumbnail((64, 64))

        self.open_img = ImageTk.PhotoImage(img)

        self.open_image_btn.configure(image=self.open_img)
        self.open_image_btn.configure(
            text=self.get_truncated_file_name(filename) + "\nImage")

    def get_truncated_file_name(self, filename, lens=20):
        filename_len = len(filename)

        if filename_len <= lens + 3:
            return filename

        return filename[:lens//2] + "..." + filename[filename_len-(lens//2):]

    def generate_btn_event(self):
        # TODO: Implement Generate Button Click Event
        pass

    # Others
    def change_appearance_mode_event(self, new_appearance_mode: str):
        ctk.set_appearance_mode(new_appearance_mode)

    # Drag and Drop
    def drop_trained_model(self, event):
        # TODO: Implement Drag and Drop Trained Model File
        print("Model:", event.data)
        self.preview_file(event.data.strip("{}"))

    def drop_image(self, event):
        # TODO: Implement Drag and Drop Image File
        print("Image:", event.data)
        self.preview_image(event.data.strip("{}"))


if __name__ == "__main__":
    app = App()
    app.mainloop()
