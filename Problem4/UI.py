import getpass
import PasswordManager
import Role
import User

class UI:
    def __init__(self) -> None:
        self.__passwordManager = PasswordManager.PasswordManager()
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
            self.loginUI()
        
        role = Role.Role(roleName)
        user = User.User(username, role)
        print("LOGIN SUCCESSFUL\n")
        print("Account information:")
        print("Username: " + user.getUsername())
        print("Role: " + role.getName())
        print("Access Permissions: ")
        perms = user.getPermissions()
        for perm in perms:
            print(perm + "=" + perms[perm])
        

    def createAccountUI(self) -> None:
        print("CREATE AN ACCOUNT")
        print("---------------------------------------")

        print("ROLE OPTIONS\n")
        print("Regular_Client\nPremium_Client\nFinancial_Advisor\nFinancial_Planner\nInvestment_Analyst\nCompliance_Officer\nTechnical_Support\nTeller\n")
        role = input("Enter Role:")
        if(role not in self.__validRoles):
            print("Invalid role entered")
            self.createAccountUI()

        username = input("Please enter unique username:")

        print("Please ensure the following")
        print("Username is unique")
        print("Password must include:")
        print("- atleast 8 characters in length")
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
            print("- atleast 8 characters in length")
            print("- one upper case letter")
            print("- one lower case letter")
            print("- one number")
            print("- one special character (!, @, #, $, %, *, ?)")
            print("- not have calendar date pattern")
            print("- not have phone number pattern")
            self.createAccountUI()

        print("ACCOUNT SUCCESSFULLY CREATED")

