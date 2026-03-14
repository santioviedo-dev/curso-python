import tkinter as tk
from tkinter import ttk

# Create window object
window = tk.Tk()
window.geometry("900x600")
window.title("New Window")
window.configure(background="#1d2d44") 

# Grid  
btn1 = ttk.Button(window, text="Button 1")
btn2 = ttk.Button(window, text="Button 2")
btn3 = ttk.Button(window, text="Button 3")

# Configurate columns
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)
window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=1)
window.rowconfigure(2, weight=1)
# This set the space that occupies each column and row

btn1.grid(row=0, column=0, sticky=tk.NSEW) # set the button position inside ther box. In this case, is set to north.
btn2.grid(row=0, column=1, ipadx=20)
btn3.grid(row=0, column=2, pady=15, ipadx=5)

window.mainloop()