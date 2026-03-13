import tkinter as tk
from tkinter import ttk

def show_text(text= None):
    label["text"] = text

# Create window object
window = tk.Tk()
window.geometry("900x600")
window.title("New Window")
window.configure(background="#1d2d44")

# Text entry widget
entry1 = ttk.Entry(window, font=("Arial", 15)) # Text box
entry1.pack(pady=40)

btn = ttk.Button(window, text="Send", command=lambda: show_text(entry1.get()))

label = ttk.Label(window, text="Waiting a message...")

btn.pack(pady=20)
label.pack(pady=20)

window.mainloop()