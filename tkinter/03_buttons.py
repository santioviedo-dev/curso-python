import tkinter as tk
from tkinter import ttk

# Create window object
window = tk.Tk()
window.geometry("900x600")
window.title("New Window")
window.configure(background="#1d2d44")

def greet():
    print("Hello")

button1 = ttk.Button(window, text="Send", command=greet) # we pass a reference of greet method/function, without parentheses. We dont execute the method.
# if we need to pass parameters to the function, we can use a lambda function for referencing indirectly the function to be executed. for exacmple:
# button1 = ttk.Button(window, text="Send", command=lambda: greet("Juan"))
button1.pack(pady=30)

window.mainloop()