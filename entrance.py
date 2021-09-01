from consoleAccess import console
from db import HP, damage
from initialization import GameLevel

class EntranceType:
    AUTHORIZATION = 1
    REGISTRATION = 2


class Entrance:

    def showMsg(self):
        pass

    def getDataFromDB(self):
        pass

class Authorization(Entrance):
    def showMsg(self):
        return 'successfully logged in'

    def getDataFromDB(self):
        data = HP, damage
        initGame = GameLevel(*data)


class Registration(Entrance):
    def showMsg(self):
        return 'registered successfully'


class ConnectionFactory:
    def createConnection(self, entranceType):
        if entranceType == EntranceType.AUTHORIZATION:
            return Authorization()
        elif entranceType == EntranceType.REGISTRATION:
            return Registration()



connect = ConnectionFactory()
loginAttempt = connect.createConnection(int(console.requestInput("Авторизация / регистрация (1/2): ")))