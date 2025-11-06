import argon2
from argon2 import PasswordHasher
ph = PasswordHasher()

def hash(password: str):
    return PasswordHasher().hash(password)

def dehash(password: str, hash: str):
    try:
        ph.verify(hash, password)
        return True
    except argon2.exceptions.VerifyMismatchError:
        return False
