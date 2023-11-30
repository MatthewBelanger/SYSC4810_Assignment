import hashlib
import random
import PasswordChecker

class PasswordManager:
    def __init__(self) -> None:
        self.__passwdFile = "passwd.txt"
        self.__passwordChecker = PasswordChecker.PasswordChecker()

    def login(self, username, passwd) -> bool:
        file = open(self.__passwdFile, "r")
        for account in file:
            account = account.split(" ")
            account[3] = account[3].replace("\n", "")
            if(account[0] == username):
                passwd = passwd + account[2]
                passwdHash = hashlib.sha512(passwd.encode())
                if (passwdHash.hexdigest() == account[3]):
                    file.close()
                    return (True, account[1])
                else:
                    print("Incorrect password")
                    file.close()
                    return (False, None)
        file.close()
        print("No account exists with that username")
        return (False, None)
                

    def createAccount(self, username, passwd, role) -> bool:
        if(not self.usernameIsUnique(username)):
            return False
        if(not self.__passwordChecker.checkPswd(username, passwd)):
            return False
        file = open(self.__passwdFile, "a")
        salt = str(random.getrandbits(32))
        passwd = passwd + salt
        passwdHash = hashlib.sha512(passwd.encode())
        file.write(username  + " " + role + " " + salt + " " + passwdHash.hexdigest() + "\n")
        file.close()
        return True
    
    def usernameIsUnique(self, username) -> bool:
        file = open(self.__passwdFile, "r")
        for line in file:
            splitLine = line.split(" ")
            if(splitLine[0] == username):
                file.close()
                print("USERNAME ALREADY EXISTS")
                return False
        file.close()
        return True

    
