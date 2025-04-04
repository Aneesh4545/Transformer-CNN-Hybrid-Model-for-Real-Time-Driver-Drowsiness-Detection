import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import os

# Initialize Tkinter Window
root = tk.Tk()
root.title("Driver Drowsiness Detection")

# Get Screen Dimensions
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry(f"{w}x{h}+0+0")
root.configure(background="#454b1b")

# Load and Set Background Image
image2 = Image.open("1.webp")
image2 = image2.resize((w, h), Image.LANCZOS)  # Updated from ANTIALIAS
background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)
background_label.pack(fill="both", expand=True)

# Title Label
title_label = tk.Label(
    root,
    text="Driver Drowsiness Detection",
    width=80,
    background="#B0E0E6",
    foreground="black",
    height=2,
    font=("Times New Roman", 25, "bold"),
)
title_label.pack()

# Button Functions
def login():
    os.system("python log.py")

def register():
    os.system("python registration.py")

# Buttons
button_style = {"width": 25, "height": 2, "bd": 0, "background": "#B0E0E6",
                "foreground": "black", "font": ("Times New Roman", 17, "bold")}

login_button = tk.Button(root, text="Login", command=login, **button_style)
login_button.place(relx=0.5, rely=0.5, anchor="center", y=-50)

register_button = tk.Button(root, text="Register", command=register, **button_style)
register_button.place(relx=0.5, rely=0.5, anchor="center", y=50)

root.mainloop()
