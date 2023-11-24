import os
import PasswordManager

def main():
    os.remove("./Problem2/passwd.txt")

    passwordManager = PasswordManager.PasswordManager()

    passwordManager.createAccount("mischa", "password123")
    passwordManager.createAccount("veronica", "password123")
    passwordManager.createAccount("winston", "password123")

    passwordManager.printFile()

main()