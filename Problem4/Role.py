import csv

class Role:
    def __init__(self, name) -> None:
        self.__name = name

    def getName(self) -> str:
        return self.__name
    
    def getPermissions(self) -> dict:
        with open("./Problem4/RolePermissionsMatrix.csv", "r") as CSVFile:
            CSVReader = csv.DictReader(CSVFile)
            dataDict = [row for row in CSVReader]
            for item in dataDict:
                role = item.pop("Role")
                if (role == self.__name):
                    return item
