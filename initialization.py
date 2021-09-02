from monsters import connectMonsterFactory
from consoleAccess import console
from time import sleep

class GameLevel:
    def __init__(self, HP, damage, countMonster=9):
        self._HP = HP
        self._damage = damage
        self._countMonster = countMonster
        while True:
            console.showMessage(self.start())

    def start(self):
        while self._countMonster != 11:
            self._normalMonster = self._createNormalMonster()
            console.showMessage(self._normalMonster.showHP())
            while self._normalMonster._HP > 0:
               console.showMessage(self.loop())
            self._HP += 3
            return 'Ты победил монстра.'

        return f'BOSS, count {self._countMonster}'

    def loop(self):
        self._normalMonster._HP -= self._damage
        if self._normalMonster._HP >= 0:
            sleep(1)
            return "У монстра {} HP.".format(self._normalMonster._HP)
        else:
            self._countMonster += 1
            return "У монстра 0 HP."


    def _createNormalMonster(self):
        return connectMonsterFactory.createNormalMonster(self._HP)

    def _onLevelFinished(self):
        pass