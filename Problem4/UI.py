import getpass
import PasswordManager
import Role
import User

class UI:
    def __init__(self) -> None:
        self.__passwordManager = PasswordManager.PasswordManager()
        self.__failedLoginAttempts = []
        self.__validRoles = ["Regular_Client", "Premium_Client", "Financial_Advisor", "Financial_Planner", "Investment_Analyst", "Compliance_Officer", "Technical_Support", "Teller"]
        self.__validActions = ['L', 'C']

    def startUI(self) -> None:
        print("\nWelcome to Finvest Holdings\n")
        action = input("Please enter L to login or C to create an account: ")
        if(action not in self.__validActions):
            print("Invalid action")
            self.startUI()
        if(action == 'C'):
            self.createAccountUI()
        elif(action == 'L'):
            self.loginUI()

    def loginUI(self) -> None:
        print("LOGIN")
        print("---------------------------------------")
        username = input("Enter username:")
        password = (getpass.getpass("Enter password:"))
        (success, roleName) = self.__passwordManager.login(username, password)
        if(not success):
            print("FAILED TO LOGIN")
            self.__failedLoginAttempts.append(username)
            if(self.__failedLoginAttempts.count(username) == 10):
                print("THIS IS YOUR 10TH FAILED LOGIN ATTEMPT IN A ROW")
                print("YOU HAVE BEEN LOCKEDOUT")
                exit()
            self.loginUI()
        role = Role.Role(roleName)
        user = User.User(username, role)
        print("LOGIN SUCCESSFUL\n")
        print("Account information:")
        print("Username: " + user.getUsername())
        print("Role: " + user.getRole())
        print("\nAccess Permissions: ")
        perms = user.getPermissions()
        for perm in perms:
            print(perm + "=" + perms[perm])

        if(user.getRole() == "Teller"):
            print("You are a teller so you can only use the system between 9:00am and 5:00pm")
        exit()
        

    def createAccountUI(self) -> None:
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
        exit()

