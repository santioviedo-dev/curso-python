import tkinter as tk

# Create window object
window = tk.Tk()
# Set window size
window.geometry("900x600")
# Set title
window.title("Nueva ventana")
# Disable resize
window.resizable(0,0)
# set background color
window.configure(background="#1d2d44")
# Init program loop
window.mainloop()