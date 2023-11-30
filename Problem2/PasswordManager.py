import hashlib
import os

class PasswordManager:
    def __init__(self) -> None:
        self.__passwdFile = "passwd.txt"

    def createAccount(self, username, passwd, role) -> bool:
        file = open(self.__passwdFile, "a")
        salt = str(os.urandom(32))
        passwd = passwd + salt
        passwdHash = hashlib.sha512(passwd.encode())
        file.write(username  + " " + role + " " + salt + " " + passwdHash.hexdigest() + "\n")
        file.close()
        return True
    
    #This method is only for testing the retrival of information from passwd.txt
    #IT WILL NOT APPEAR IN FINAL VERSION OF SYSTEM
    def printFile(self) -> None:
        file = open(self.__passwdFile, "r")
        for line in file:
            print(line)
