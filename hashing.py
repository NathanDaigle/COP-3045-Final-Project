import argon2

def hash(password: str):
    return argon2.PasswordHasher().hash(password)

def dehash(password: str, hash: str):
    ph = argon2.PasswordHasher()
    try:
        ph.verify(hash, password)
        return True
    except argon2.exceptions.VerifyMismatchError:
        return False
