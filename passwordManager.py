import hashing
import json

def addPassword(password: str):
    pass

def fetchPassword(serviceName: str):
    Passwords = json.loads(open("Passwords.json", "r").read())
    masterKey = Passwords["Master"]
    pass