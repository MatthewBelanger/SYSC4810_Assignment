import hashlib
import random
import PasswordChecker

class PasswordManager:
    def __init__(self) -> None:
        self.__passwdFile = "passwd.txt"
        self.__passwordChecker = PasswordChecker.PasswordChecker()

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

    
