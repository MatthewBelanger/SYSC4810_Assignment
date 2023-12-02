class PasswordChecker:
    def __init__(self) -> None:
        '''
        Based on examples given from assignment as well as a list of 20 most common passwords by readers digest
        https://www.rd.com/article/passwords-hackers-guess-first/
        '''
        self.__weakPswdLst = ["Password1!", "Qwert123!", "Qaz123%wsx", "12345678", "admin123",
                    "123456789", "password", "Aa123456", "1234567890", "UNKNOWN!",
                    "Password", "12345678910", "********", "123456", "Qwerty", "12345", "111111",
                    "1234567", "123123", "Qwerty123", "1q2w3e", "1234567890", "DEFAULT", "Abc123",
                    "654321", "123321", "Qwertyuiop", "Iloveyou"]
        
    def checkPswd(self, username, passwd) -> bool:
        if (len(passwd) < 8 or len(passwd) > 1024):
            return False
        if passwd in self.__weakPswdLst:
            return False
        if (passwd == username):
            return False
        if(self.isCalenderDateOrPhoneNumber(passwd)):
            return False
        return self.containsRequiredCharacters(passwd)
        
    #Any password containing exactly 8 or 9 numbers will not be allowed
    #in fear they are a phone number or a date
    def isCalenderDateOrPhoneNumber(self, passwd) -> bool:
        if (len(passwd) > 9):
            return False
        numberCount = 0
        for elem in passwd:
            if (elem.isnumeric()):
                numberCount += 1
        if(numberCount == 8 or numberCount == 9):
            return True
        return False
    
    def containsRequiredCharacters(self, passwd) -> bool:
        containsNumber = False
        containsUpper = False
        containsLower = False
        containsSpecial = False
        specialCharacters = ["!", "@", "#", "$", "%", "?", "*"]
        for elem in passwd:
            if(elem.isnumeric()):
                containsNumber = True
            elif(elem.isupper()):
                containsUpper = True
            elif(elem.islower()):
                containsLower = True
            elif(elem in specialCharacters):
                containsSpecial = True

            if(containsNumber and containsUpper and containsLower and containsSpecial):
                return True
        return False