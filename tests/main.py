import tkinter

import customtkinter

from tkinterdnd2 import DND_FILES, TkinterDnD

def drop_inside_list_box(event):
    textbox.insert("end", event.data)
    print(event.data)


# def get_path(event):
#     pathLabel.configure(text = event.data)

# https://stackoverflow.com/questions/75526264/using-drag-and-drop-files-or-file-picker-with-customtkinter
# For Drag and Drop in customtkinter
class Tk(customtkinter.CTk, TkinterDnD.DnDWrapper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.TkdndVersion = TkinterDnD._require(self)

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

# app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app = Tk()  # create CTk window like you do with the Tk window
app.geometry("400x240")

# create textbox
textbox = customtkinter.CTkTextbox(app, width=250)
# textbox.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
textbox.pack(fill=tkinter.X)

# listb = tkinter.Tk.listbox(app, selectmode=tkinter.SINGLE, background="#ffe0d6")
# listb.pack(fill=tkinter.X)
textbox.drop_target_register(DND_FILES)
textbox.dnd_bind("<<Drop>>", drop_inside_list_box)

def button_function():
    print("button pressed")

# Use CTkButton instead of tkinter Button
button = customtkinter.CTkButton(master=app, text="CTkButton", command=button_function)
button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

app.mainloop()