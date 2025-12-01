import os
import json
from tkinter import messagebox, simpledialog
import tkinter as tk
from hashing import hashPassword, verifyPassword
from passwordManager import vaultInit, loadData
from ui import MainUI

def get_master_password(prompt: str = "Enter master password:"):
    """Retrives master password from user with a dialog popup."""
    root = tk.Tk()
    root.withdraw()
    password = simpledialog.askstring("Master Password", prompt, show="*", parent=root)
    root.destroy()
    return password

def main():
    """Responsible for first-time setup and running the UI"""
    DATA_FILE = "Passwords.json"

    if not os.path.exists(DATA_FILE):
        # First-time setup
        messagebox.showinfo("First Run", "Create your master password.")
        master = get_master_password("Enter master password:")
        if master:
            confirm = get_master_password("Confirm master password:")
            if master == confirm:
                vaultInit(master)
                messagebox.showinfo("Success", "Vault created!")
            else:
                messagebox.showerror("Error", "Passwords don't match. Exiting.")
                return
        else:
            return

    # Login loop
    while True:
        master = get_master_password("Enter master password to login:")
        if not master:
            continue
        try:
            data = loadData()
            if verifyPassword(master, data["master_hash"]):
                # Launch UI
                app = MainUI(master)
                app.run()
                break
            else:
                messagebox.showerror("Error", "Invalid master password.")
        except Exception as e:
            messagebox.showerror("Error", f"Login failed: {e}")

if __name__ == "__main__":
    main()