import argon2
from argon2 import PasswordHasher
from argon2.low_level import hash_secret_raw, Type
import base64

ph = PasswordHasher()

def hashPassword(password: str):
    return PasswordHasher().hash(password)

def verifyPassword(password: str, hashed: str):
    try:
        ph.verify(hashed, password)
        return True
    except:
        return False

def dehash(password: str, hash: str):
    try:
        ph.verify(hash, password)
        return True
    except argon2.exceptions.VerifyMismatchError:
        return False
    
def derive_key(password: str, salt: bytes, hash_len=32):
    time_cost = 2
    memory_cost = 65536
    parallelism = 8
    key_bytes = hash_secret_raw(
        secret=password.encode(),
        salt=salt,
        time_cost=time_cost,
        memory_cost=memory_cost,
        parallelism=parallelism,
        hash_len=hash_len,
        type=Type.ID,
    )
    encoded_key = base64.urlsafe_b64encode(key_bytes)
    return encoded_key