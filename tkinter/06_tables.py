import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# Create window object
window = tk.Tk()
window.geometry("900x600")
window.title("New Window")
window.configure(background="#1d2d44") 

window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=0)

# Styles
styles = ttk.Style()
styles.theme_use("clam") # prepare black theme use
styles.configure("Treeview", background="black", foreground="white", fieldbackground="black", rowheight=30) 

styles.map("Treeview", background=[("selected", "#3a86ff")])

# Define columns and init table
columns = ("Id", "Name", "Age")
table = ttk.Treeview(window, columns=columns, show="headings")

# Setting columns
table.heading("Id", text="Id", anchor=tk.CENTER)
table.heading("Name", text="Name", anchor=tk.W)
table.heading("Age", text="Age", anchor=tk.W)

# Formatting columns
table.column("Id", width=80) 
table.column("Name", width=120) 
table.column("Age", width=80) 

# Insert data
data = ((1, "Alejandro", 25), (2, "Matías", 19))

# data = ((1, "Alejandro", 25), (2, "Matías", 19)) + ((1, "Alejandro", 25), (2, "Matías", 19)) + ((1, "Alejandro", 25), (2, "Matías", 19)) + ((1, "Alejandro", 25), (2, "Matías", 19)) + ((1, "Alejandro", 25), (2, "Matías", 19)) + ((1, "Alejandro", 25), (2, "Matías", 19))

for person in data:
    table.insert(parent="", index=tk.END, values=person)

scrollbar = ttk.Scrollbar(window, orient=tk.VERTICAL, command=table.yview)
table.configure(yscroll=scrollbar.set)
scrollbar.grid(row=0, column=1, sticky=tk.NS)

def showselected(event):
    selected = table.selection()[0]
    item = table.item(selected)
    person = item["values"]
    showinfo(title="Registro seleccionado", message=f"""Id: {person[0]} Name: {person[1]} Age: {person[2]}
             """)

table.bind("<<TreeviewSelect>>", showselected)

# Show table
table.grid(row=0, column=0, sticky=tk.NSEW)



window.mainloop()