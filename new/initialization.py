from monsters import connectMonsterFactory
from consoleAccess import console

class GameLevel:
    def __init__(self, HP, damage, countMonster=0):
        self._HP = HP
        self._damage = damage
        self._countMonster = countMonster
        console.showMessage(self.start())

    def start(self):
        self._monster = connectMonsterFactory.createNormalMonster(self._HP)
        console.showMessage(self._monster.showHP())
        while self._monster._HP > 0:
           console.showMessage(self.loop())
        return 'Ты победил монстра.'

    def loop(self):
        self._monster._HP -= self._damage
        if self._HP >= 0:
            return "У монстра {} HP.".format(self._monster._HP)
        else:
            self._countMonster += 1


    def _onLevelFinished(self):
        pass