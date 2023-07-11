import os
from tkinter import *
from tkinter import colorchooser, font
from tkinter.filedialog import *
from tkinter.messagebox import *


def new_file():
    global file

    if len(text_area.get("1.0", END + "-1c")) > 0:
        if askyesno("Notepad", "Do you want to save changes?"):
            save_file()

        else:
            file.close()
            file = None
            text_area.delete(1.0, END)
            window.title("Untitled - Notepad")


def open_file():
    global file
    file = askopenfilename(
        title="Open File",
        initialdir="/",
        defaultextension=".txt",
        filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")],
    )

    if file is None or file == "":
        return

    else:
        try:
            window.title(os.path.basename(f"{file} - Notepad"))
            text_area.delete(1.0, END)
            file = open(file, "r+")
            text_area.insert(1.0, file.read())
            text_area.focus()

        except Exception:
            showerror(title="Error", message="Couldn't read file!")


def saveAs_file():
    global file
    file = asksaveasfilename(
        title="Save As",
        initialfile="Untitled.txt",
        defaultextension=".txt",
        initialdir="/",
        filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")],
    )
    if file is None or file == "":
        return

    else:
        try:
            window.title(os.path.basename(f"{file} - Notepad"))
            file = open(file, "w")
            file.write(text_area.get(1.0, END))

        except Exception:
            showerror(title="Error", message="Couldn't save file.")


def save_file():
    global file
    try:
        if file is not None:
            file.seek(0)
            file.truncate(0)
            file.write(text_area.get(1.0, END))

        else:
            saveAs_file()

    except Exception:
        showerror(title="Error", message="Couldn't save file.")


def change_font(*args):
    text_area.config(font=(font_name.get(), font_size.get()))


def change_color():
    color = colorchooser.askcolor(title="Pick a color")
    text_area.config(foregrou=color[1])


def change_bg():
    bg = colorchooser.askcolor(title="Pick a color")
    text_area.config(background=bg[1])


def copy():
    text_area.event_generate("<<Copy>>")


def cut():
    text_area.event_generate("<<Cut>>")


def paste():
    text_area.event_generate("<<Paste>>")


def about():
    showinfo(title="About", message="This program was made by Coolitoyce.")


window = Tk()
window.title("Untitled - Notepad")
window.geometry("600x500")

file = None

font_name = StringVar(window)
font_name.set("Arial")

font_size = StringVar(window)
font_size.set("25")

text_area = Text(window, font=("Consolas", 20))
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
text_area.grid(sticky=N + S + W + E)

scroll_bar = Scrollbar(text_area)
scroll_bar.pack(side=RIGHT, fill=Y)
text_area.config(yscrollcommand=scroll_bar.set)

frame = Frame()
frame.grid()

font_box = OptionMenu(frame, font_name, *font.families(), command=change_font)
font_box.grid(row=0, column=0, padx=5)

color_button = Button(frame, text="Color", command=change_color)
color_button.grid(row=0, column=1, padx=5)

size_box = Spinbox(frame, from_=0, to=100, textvariable=font_size, command=change_font)
size_box.grid(row=0, column=2, padx=5)

bg_button = Button(frame, text="Background", command=change_bg)
bg_button.grid(row=0, column=3, padx=5)
menu_bar = Menu(window)
window.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(menu=file_menu, label="File")
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Save As", command=saveAs_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=quit)

edit_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Copy", command=copy)
edit_menu.add_command(label="Cut", command=cut)
edit_menu.add_command(label="Paste", command=paste)

help_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=about)

window.mainloop()
