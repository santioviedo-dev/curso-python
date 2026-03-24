import tkinter as tk
from tkinter import ttk
from clientDAO import ClientDAO

class App(tk.Tk):
    WINDOW_COLOR = "#1d2d44"
    
    def __init__(self):
        super().__init__()
        self.configure_window()
        self.configure_grid()
        self.show_title()
        self.show_form()
        self.show_table()
        
    def configure_window(self):
        self.geometry("900x600")
        self.title("Fit Zone App")
        self.configure(background=App.WINDOW_COLOR)
        # Styles
        self.styles = ttk.Style()
        self.styles.theme_use("clam")
        self.styles.configure(self, background=App.WINDOW_COLOR, foreground="white", fillbackground="black")
        
    def configure_grid(self):
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
    
    def show_title(self):
        label = ttk.Label(self, text="Fit Zone (GYM)", font=("Arial", 22), background=App.WINDOW_COLOR, foreground="white")
        label.grid(row=0, column=0, columnspan=2, pady=30)
        
    def show_form(self):
        pass
    
    def show_table(self):
        self.frame_table = ttk.Frame(self)
        self.styles.configure(
            "Treeview",
            background="black",
            foreground="white",
            fillbackground="black",
            rowheight=20
        )
        columns = ("Id", "First name", "Last name", "Membership")
        self.table = ttk.Treeview(self.frame_table, columns=columns, show="headings")
        
        self.table.heading("Id", text="Id", anchor=tk.CENTER)
        self.table.heading("First name", text="First name", anchor=tk.W)
        self.table.heading("Last name", text="Last name", anchor=tk.W)
        self.table.heading("Membership", text="Membership", anchor=tk.W)
        
        self.table.column("Id", anchor=tk.CENTER, width=50)
        self.table.column("First name", anchor=tk.W, width=100)
        self.table.column("Last name", anchor=tk.W, width=100)
        self.table.column("Membership", anchor=tk.W, width=100)
        
        clients = ClientDAO.select()
        for client in clients:
            self.table.insert(parent="", index=tk.END, values=(client.id, client.first_name, client.last_name, client.membership))
            
        scrollbar = ttk.Scrollbar(self.frame_table, orient=tk.VERTICAL, command=self.table.yview)
        self.table.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky=tk.NS)
        
        self.table.grid(row=0, column=0)
        self.frame_table.grid(row=1, column=1, padx=20)
    


if __name__ == "__main__":
    app = App()
    app.mainloop()