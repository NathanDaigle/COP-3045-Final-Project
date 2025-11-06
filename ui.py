import tkinter as tk
from tkinter import messagebox

class MainUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("SecureLock")
        self.root.geometry("500x300")
        self.root.resizable(False, False)

        self.label = tk.Label(self.root, text="Hello World!")
        self.label.pack(pady=20, padx=20)

        self.quit_button = tk.Button(self.root, text="Quit", command=self.root.quit)
        self.quit_button.pack(pady=10)

    def on_click(self):
        messagebox.showinfo("Info", "Button clicked!")

    def run(self):
        self.root.mainloop()