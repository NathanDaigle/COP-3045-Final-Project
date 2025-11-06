import ui
import hashing
import secrets
import json
import os
import passwordManager as PM

def main():
    if not os.path.exists("Passwords.json"): # new user / missing file
        with open("Passwords.json", "x+")  as f:
            temp = {
                "Master": secrets.token_urlsafe(64)
            }
            f.write(json.dumps(temp))
            
    # ideally should never throw an error but try is always good
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