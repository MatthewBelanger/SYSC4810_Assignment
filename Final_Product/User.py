import Role

class User:
    def __init__(self, username, role) -> None:
        self.__username = username
        self.__role = role

    def getUsername(self) -> str:
        return self.__username
    
    def getRole(self) -> Role:
        return self.__role.getName()

    def getPermissions(self) -> dict:
        return self.__role.getPermissions()