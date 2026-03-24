import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.configure_window()
        self.configure_grid()
        self.show_table()
    
    def configure_window(self):
        self.geometry("600x400")
        self.configure(background="#1d2d44")
        self.title("Window management with POO")
    
    def configure_grid(self):
        self.columnconfigure(0, weight=1)
        self.columnconfigure(0, weight=0)
       
    def show_table(self):
        # Styles
        styles = ttk.Style()
        styles.theme_use("clam") # prepare black theme use
        styles.configure("Treeview", background="black", foreground="white", fieldbackground="black", rowheight=30) 

        styles.map("Treeview", background=[("selected", "#3a86ff")]) 
        
        
        # Define columns and init table
        columns = ("Id", "Name", "Age")
        self.table = ttk.Treeview(self, columns=columns, show="headings")

        # Setting columns
        self.table.heading("Id", text="Id", anchor=tk.CENTER)
        self.table.heading("Name", text="Name", anchor=tk.W)
        self.table.heading("Age", text="Age", anchor=tk.W)  
        
        # Formatting columns
        self.table.column("Id", width=80) 
        self.table.column("Name", width=120) 
        self.table.column("Age", width=80) 
        
        # Insert data
        data = ((1, "Alejandro", 25), (2, "Matías", 19))
        
        for person in data:
            self.table.insert(parent="", index=tk.END, values=person)
            
        scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.table.yview)
        self.table.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky=tk.NS)
        
        self.table.bind("<<TreeviewSelect>>", self.showselected)
        
        # Show table
        self.table.grid(row=0, column=0, sticky=tk.NSEW)
    
    def showselected(self, event):
        selected = self.table.selection()[0]
        item = self.table.item(selected)
        person = item["values"]
        showinfo(title="Registro seleccionado", message=f"""Id: {person[0]} Name: {person[1]} Age: {person[2]}
                """)
     
    
if __name__ == "__main__":
    app = App()
    app.mainloop( )