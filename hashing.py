import argon2

def hash(password):
    return argon2.PasswordHasher().hash(password)

def dehash(password, hash):
    ph = argon2.PasswordHasher()
    try:
        ph.verify(hash, password)
        return True
    except argon2.exceptions.VerifyMismatchError:
        return False
