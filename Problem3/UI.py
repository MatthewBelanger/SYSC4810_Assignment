import getpass
import PasswordManager

class UI:
    def __init__(self) -> None:
        self.__passwordManager = PasswordManager.PasswordManager()
        self.__validRoles = ["Regular_Client", "Premium_Client", "Financial_Advisor", "Financial_Planner", "Investment_Analyst", "Compliance_Officer", "Technical_Support", "Teller"]

    def createAccountUI(self) -> None:
        print("\nFinvest Holdings")
        print("CREATE AN ACCOUNT")
        print("---------------------------------------")

        print("ROLE OPTIONS\n")
        for role in self.__validRoles:
            print(role)
        role = input("Enter Role:")
        if(role not in self.__validRoles):
            print("Invalid role entered")
            self.createAccountUI()

        username = input("Please enter unique username:")

        print("Please ensure the following")
        print("Username is unique")
        print("Password must include:")
        print("- Between 8 to 1024 characters in length")
        print("- one upper case letter")
        print("- one lower case letter")
        print("- one number")
        print("- one special character (!, @, #, $, %, *, ?)")
        print("- not have calendar date pattern")
        print("- not have phone number pattern")
        password = (getpass.getpass("Enter password:"))

        if(not self.__passwordManager.createAccount(username, password, role)):
            print("FAILED TO CREATE ACCOUNT\n")
            print("Please ensure the following")
            print("Username is unique")
            print("Password must include:")
            print("- Between 8 to 1024 characters in length")
            print("- one upper case letter")
            print("- one lower case letter")
            print("- one number")
            print("- one special character (!, @, #, $, %, *, ?)")
            print("- not have calendar date pattern")
            print("- not have phone number pattern")
            self.createAccountUI()
        print("ACCOUNT SUCCESSFULLY CREATED")

