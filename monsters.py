class MonsterType:
    NORMAL = 1
    BOSS = 2


class Monster:
    def showHP(self):
        pass


class NormalMonster(Monster):
    def __init__(self, HP):
        self._HP = HP
        self.showHP()

    def showHP(self):
        return "У монстра {} HP.".format(self._HP)


class BossMonster(Monster):
    def __init__(self, HP):
        self._HP = HP * 2
        self.showHP()

    def showHP(self):
        return "У монстра {} HP.".format(self._HP)


class MonsterFactory:
    def createNormalMonster(self, HP):
        return NormalMonster(HP)

    def createBossMonster(self, HP):
        return BossMonster(HP)


connectMonsterFactory = MonsterFactory()