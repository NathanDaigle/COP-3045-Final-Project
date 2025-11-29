import tkinter as tk
from passwordManager import addPassword, fetchPassword, deletePassword, listServices, vaultInit
from tkinter import messagebox

class MainUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("SecureLock")
        self.root.geometry("500x300")
        self.root.resizable(False, False)

        self.label = tk.Label(self.root, text="Test Label")
        self.label.pack(pady=20, padx=20)

    def on_click(self):
        messagebox.showinfo("Info", "Button clicked!")

    def run(self):
        self.root.mainloop()