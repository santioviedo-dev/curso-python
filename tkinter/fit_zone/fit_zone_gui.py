import tkinter as tk
from tkinter import ttk
from clientDAO import ClientDAO
from tkinter.messagebox import showerror, showinfo
from client import Client

class App(tk.Tk):
    WINDOW_COLOR = "#1d2d44"
    
    def __init__(self):
        super().__init__()
        self.client_id = None
        self.configure_window()
        self.configure_grid()
        self.show_title()
        self.show_form()
        self.load_table()
        self.show_buttons()
        
    def configure_window(self):
        self.geometry("900x600")
        self.title("Fit Zone App")
        self.configure(background=App.WINDOW_COLOR)
        # Styles
        self.styles = ttk.Style()
        self.styles.theme_use("clam")
        self.styles.configure(self, background=App.WINDOW_COLOR, foreground="white", fieldbackground="black")
        
    def configure_grid(self):
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
    
    def show_title(self):
        label = ttk.Label(self, text="Fit Zone (GYM)", font=("Arial", 22), background=App.WINDOW_COLOR, foreground="white")
        label.grid(row=0, column=0, columnspan=2, pady=30)
        
    def show_form(self):
        self.frame_form = ttk.Frame(self)
        
        first_name_label = ttk.Label(self.frame_form, text="Nombre: ")
        first_name_label.grid(row=0, column=0, sticky=tk.W, pady=30, padx=5)
        self.first_name_entry =ttk.Entry(self.frame_form)
        self.first_name_entry.grid(row=0, column=1)

        last_name_label = ttk.Label(self.frame_form, text="Apellido: ")
        last_name_label.grid(row=1, column=0, sticky=tk.W, pady=30, padx=5)
        self.last_name_entry =ttk.Entry(self.frame_form)
        self.last_name_entry.grid(row=1, column=1)

        membership_label = ttk.Label(self.frame_form, text="Membresía: ")
        membership_label.grid(row=2, column=0, sticky=tk.W, pady=30, padx=5)
        self.membership_entry =ttk.Entry(self.frame_form)
        self.membership_entry.grid(row=2, column=1)
        
        
        self.frame_form.grid(row=1, column=0)
        
    def show_buttons(self):
        self.frame_buttons = ttk.Frame()
        
        add_button = ttk.Button(self.frame_buttons, text="Guardar", command=self.validate)
        add_button.grid(row=0, column=0, sticky=tk.W, padx=30)

        delete_button = ttk.Button(self.frame_buttons, text="Eliminar", command=self.delete)
        delete_button.grid(row=0, column=1, sticky=tk.W, padx=30)

        add_button = ttk.Button(self.frame_buttons, text="Limpiar", command=self.clean_data)
        add_button.grid(row=0, column=2, sticky=tk.W, padx=30)
        
        self.styles.configure("TButton", background="#005f73")
        self.styles.map("TButton", background=[("active", "#0a9396")])
        
        self.frame_buttons.grid(row=2, column=0, columnspan=2, pady=20)
        
    
    def load_table(self):
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
        
        self.table.bind("<<TreeviewSelect>>", self.load_client)
        
        self.table.grid(row=0, column=0)
        self.frame_table.grid(row=1, column=1, padx=20)
    
    def validate(self):
        if(not self.first_name_entry.get() or not self.last_name_entry.get() or not self.membership_entry.get()):
            showerror(title="Atención", message="Debe llenar el formulario.")
            self.first_name_entry.focus_set()
            return
            
        if not self.membership_is_int():
            showerror(title="Atención", message="El valor de membresía debe ser numérico.")
            self.membership_entry.delete(0, tk.END)
            self.membership_entry.focus_set()
            return
        
        self.insert()
        
            
    def membership_is_int(self):
        try:
            int(self.membership_entry.get())
            return True
        except:
            return False
    def insert(self):
        first_name, last_name, membership = (
            self.first_name_entry.get(),
            self.last_name_entry.get(),
            self.membership_entry.get()
        )
        if self.client_id is None: 
            client = Client(first_name=first_name, last_name=last_name, membership=membership)
            ClientDAO().insert(client)
            showinfo(title="Agregar", message="¡Cliente agregado!")
        else:
            client = Client(self.client_id, first_name=first_name, last_name=last_name, membership=membership)
            ClientDAO.update(client)
            showinfo(title="Actualizar", message="Cliente actualizado") 
        self.reload_table()
    def load_client(self, event):
        selected = self.table.selection()[0]
        item = self.table.item(selected)
        client = item["values"]
        self.client_id, first_name, last_name, membership = client
        self.clean_form()
        
        self.first_name_entry.insert(0, first_name)
        self.last_name_entry.insert(0, last_name)
        self.membership_entry.insert(0, membership)
        
    def reload_table(self):
        self.load_table()
        self.clean_data()
    def delete(self):
        if self.client_id is None:
            showerror(title="Atención", message="Debes seleccionar un cliente para eliminar.")
            return
        else:
            ClientDAO().delete(self.client_id)
            showinfo(title="Eliminar", message="Cliente eliminado.")
            self.reload_table()
    def clean_data(self):
        self.clean_form()
        self.client_id = None
    def clean_form(self):
        self.first_name_entry.delete(0, tk.END)
        self.last_name_entry.delete(0, tk.END)
        self.membership_entry.delete(0, tk.END)


if __name__ == "__main__":
    app = App()
    app.mainloop()