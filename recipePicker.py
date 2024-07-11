"""Recipe Picker"""
import tkinter as tk
from PIL import ImageTk
import tkmacosx as tkx
from tkmacosx import Button


# variables
bg_color = "#3d6466"

# functions
def load_frame2():
    """Load frame2 when button is clicked"""
    print("Hello from frame2")

# initiallize window opject we are calling loop
root = tk.Tk()
root.title("Recipe Picker")
# eval method is used to execute a command in the tcl interpreter
root.eval("tk::PlaceWindow . center")

# create a frame widget
frame1 = tk.Frame(root, width=500, height=600, bg=bg_color)
frame1.grid(row=0, column=0)
frame1.pack_propagate(False)

# frame1 widgets
logo_img = ImageTk.PhotoImage(file="assets/RRecipe_logo.png")
logo_widget = tk.Label(frame1, image=logo_img, bg=bg_color)
logo_widget.image = logo_img
logo_widget.pack()

tk.Label(
    frame1,
    text="ready for your random recipe?",
    bg=bg_color,
    fg="white",
    font=("TkMenuFont", 14),
).pack()

# button widget
tkx.Button(
    frame1,
    text="Pick a Recipe",
    font=("TkHeadingFont", 20),
    bg="#28393a",
    fg="white",
    cursor="hand2",
    activebackground="#badee2",
    activeforeground="black",
    command=load_frame2(),
).pack()

# call mainloop method that displays our window untill we hit the Exit button
root.mainloop()