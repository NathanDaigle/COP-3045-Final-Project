import json
import os
from cryptography.fernet import Fernet
from hashing import derive_key, verifyPassword, hashPassword

DATA_FILE = "Passwords.json"

def loadData():
    if not os.path.exists(DATA_FILE):
        raise FileNotFoundError("Vault not initialized. Run first-time setup.")
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

def saveData(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

def vaultInit(master_password: str):
    """First-time setup: Create vault with hashed master and salt."""
    data = {
        "master_hash": hashPassword(master_password),  # From hashing
        "salt": os.urandom(16).hex(),
        "entries": {}
    }
    saveData(data)

def add_password(service: str, password: str, master_password: str):
    """Add encrypted password for service."""
    try:
        data = loadData()
        if not verifyPassword(master_password, data["master_hash"]):
            raise ValueError("Invalid master password.")
        salt = bytes.fromhex(data["salt"])
        key = derive_key(master_password, salt)
        f = Fernet(key)
        enc_pass = f.encrypt(password.encode()).decode()
        data["entries"][service] = enc_pass
        saveData(data)
        return True
    except Exception:
        return False

def fetchPassword(serviceName: str):
    Passwords = json.loads(open("Passwords.json", "r").read())
    masterKey = Passwords["Master"]
    pass