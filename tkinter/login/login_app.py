import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo, showerror

def validate(event):
    user = user_entry.get()
    password = password_entry.get()
    if user == "root" and password == "admin":
        showinfo(title="Login", message="Datos correctos")
    else:
        showerror(title="Login", message="¡Datos incorrectos!")

window = tk.Tk()
window.geometry("600x400")
window.title("Login")
window.configure(background="#1d2d44") 

window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)

# Define styles
styles = ttk.Style()
styles.theme_use("clam")
# styles.configure(window, background="1d2d44", foreground="white", fieldbackground="black")
# styles.configure("TButton", background=[("active", "#0a9396")])

# Frame
frame = ttk.Frame(window) # Parent
frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=3)

frame.grid(row=0, column=0)

label = ttk.Label(frame, text="Login", font=("Arial", 20))
user_label = ttk.Label(frame, text="User: ")
user_entry = ttk.Entry(frame)
password_label = ttk.Label(frame, text="Password: ")
password_entry = ttk.Entry(frame, show="*")
button = ttk.Button(frame, text="Send")

# asociate events to login button
button.bind("<Return>", validate)
button.bind("<Button-1>", validate)



button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
user_entry.grid(row=1, column=1, sticky=tk.E, padx=5, pady=5)
user_label.grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
password_entry.grid(row=2, column=1, sticky=tk.E, padx=5, pady=5)
password_label.grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)
label.grid(row=0, column=0, columnspan=2)
window.mainloop()