from monsters import connectMonsterFactory
from consoleAccess import console
from time import sleep

class GameLevel:
    def __init__(self, HP, damage, countMonster=10):
        self._HP = HP
        self._damage = damage
        self._countMonster = countMonster
        while True:
            self.start() 

    def someLoop(self):
        while self._monster._HP > 0:
            console.showMessage(self.loop())
        self._HP += 3
        if self._countMonster != 11:
            return 'Ты победил монстра.'
        else:
            self._countMonster = 0
            return 'Ты победил Монстр-Босса!'

    def start(self):
        while self._countMonster < 11:
            self._monster = self._createNormalMonster()
            console.showMessage(self._monster.showHP())
            console.showMessage(self.someLoop())
        else:
            self._monster = self._createBoosMonster()
            console.showMessage(self._monster.showHP())
            console.showMessage(self.someLoop())       

    def loop(self):
        self._monster._HP -= self._damage
        if self._monster._HP >= 0:
            sleep(1)
            return "У монстра {} HP.".format(self._monster._HP)
        else:
            self._countMonster += 1
            return "У монстра 0 HP."

    def _createNormalMonster(self):
        return connectMonsterFactory.createNormalMonster(self._HP)

    def _createBoosMonster(self):
        return connectMonsterFactory.createBossMonster(self._HP)

    def _onLevelFinished(self):
        pass