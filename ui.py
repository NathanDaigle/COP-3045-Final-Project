import tkinter as tk
from tkinter import messagebox, simpledialog
from passwordManager import addPassword, fetchPassword, deletePassword, listServices, vaultInit

class MainUI:
    def __init__(self, master_password: str):
        self.master_password = master_password
        self.root = tk.Tk()
        self.root.title("SecureLock")
        self.root.geometry("500x400")
        self.root.resizable(False, False)

        self.setup_ui()

    def setup_ui(self):
        # Title
        title = tk.Label(self.root, text="SecureLock Password Manager", font=("Arial", 16))
        title.pack(pady=10)

        # Services Listbox
        tk.Label(self.root, text="Services:").pack()
        self.listbox = tk.Listbox(self.root, height=10)
        self.listbox.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)
        self.update_list()

        # Buttons
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Add Password", command=self.add_entry).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Fetch Password", command=self.fetch_entry).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Delete Service", command=self.delete_entry).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Logout", command=self.logout).pack(side=tk.RIGHT, padx=5)

    def update_list(self):
        self.listbox.delete(0, tk.END)
        services = listServices(self.master_password)
        for service in services:
            self.listbox.insert(tk.END, service)

    def add_entry(self):
        service = simpledialog.askstring("Add Service", "Enter service name:")
        if service:
            password = simpledialog.askstring("Add Password", "Enter password:", show="*")
            if password and addPassword(service, password, self.master_password):
                messagebox.showinfo("Success", "Password added!")
                self.update_list()
            else:
                messagebox.showerror("Error", "Failed to add password.")

    def fetch_entry(self):
        selection = self.listbox.curselection()
        if selection:
            service = self.listbox.get(selection[0])
            password = fetchPassword(service, self.master_password)
            if password:
                messagebox.showinfo(f"Password for {service}", f"Password: {password}")
            else:
                messagebox.showerror("Error", "Failed to retrieve password.")
        else:
            messagebox.showwarning("Warning", "Select a service!")

    def delete_entry(self):
        selection = self.listbox.curselection()
        if selection:
            service = self.listbox.get(selection[0])
            if deletePassword(service, self.master_password):
                messagebox.showinfo("Success", "Service deleted!")
                self.update_list()
            else:
                messagebox.showerror("Error", "Failed to delete.")
        else:
            messagebox.showwarning("Warning", "Select a service!")

    def logout(self):
        self.root.quit()

    def run(self):
        self.root.mainloop()