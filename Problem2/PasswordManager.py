import hashlib
import random

class PasswordManager:
    def __init__(self) -> None:
        self.__passwdFile = "./Problem2/passwd.txt"

    def createAccount(self, username, passwd) -> bool:
        file = open(self.__passwdFile, "a")
        salt = str(random.getrandbits(32))
        passwd = passwd + salt
        passwdHash = hashlib.sha512(passwd.encode())
        file.write(username  + " " + salt + " " + passwdHash.hexdigest() + "\n")
        file.close()
        return True
    
    #This method is only for testing the retrival of information from passwd.txt
    #IT WILL NOT APPEAR IN FINAL VERSION OF SYSTEM
    def printFile(self) -> None:
        file = open(self.__passwdFile, "r")
        for line in file:
            print(line)
