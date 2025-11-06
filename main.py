import ui
import hashing

def main():
    unhashed = "testPassword123"
    hashed = hashing.hash(unhashed)
    print("Hashing Test: ", hashed)
    print("Is Hash valid? ", hashing.dehash(unhashed, hashed))

    app = ui.MainUI()
    app.run()

if __name__ == "__main__":
    main()