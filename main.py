import os
import json
from tkinter import messagebox, simpledialog
import tkinter as tk
from hashing import hashPassword, verifyPassword
from passwordManager import vaultInit, loadData
from ui import MainUI

def main():
    if not os.path.exists("Passwords.json"): # New user / Missing file
        with open("Passwords.json", "x+")  as f:
            temp = {
                "Master": secrets.token_urlsafe(64)
            }
            f.write(json.dumps(temp))
            
    # Ideally should never throw an error but try is always good
    try:
        # format {"Master": "masterKey", "ServiceName": "HashedPassword"}
        currentPasswords = json.loads(open("Passwords.json", "r").read())
    except FileNotFoundError:
        print("Passwords.json not found!")
        exit(1)
    print(currentPasswords)
    
    # app = ui.MainUI()
    # app.run()

if __name__ == "__main__":
    main()