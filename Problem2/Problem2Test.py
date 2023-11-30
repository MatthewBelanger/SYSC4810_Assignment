import PasswordManager

def main():
    passwordManager = PasswordManager.PasswordManager()

    passwordManager.createAccount("mischa", "password123", "Regular_Client")
    passwordManager.createAccount("veronica", "password123", "Regular_Client")
    passwordManager.createAccount("winston", "password123", "Teller")

    passwordManager.printFile()

main()