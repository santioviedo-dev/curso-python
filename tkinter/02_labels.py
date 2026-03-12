import tkinter as tk
from tkinter import ttk

# Create window object
window = tk.Tk()
# Set window size
window.geometry("900x600")
# Set title
window.title("Nueva ventana")
# set background color
window.configure(background="#1d2d44")

# Create label 
# label = tk.Label(window, text="Saludos") # in this case, window is the parent of label
# Using ttk
label = ttk.Label(window, text="Saludos") # in this case, window is the parent of label

# pack is for placing the label within the interface
label.pack(pady=20, padx=50)

# Set text after create with configure method
label.configure(text="See you later...")

# Set text after create with text key
label["text"] = "Bye"

# Init program loop
window.mainloop()