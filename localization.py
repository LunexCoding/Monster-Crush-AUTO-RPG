class Parameters:
    def showCoins(self):
        return {
            coins % 10 == 1 and coins != 11: 'монета',
            2 <= coins % 10 <= 4 and coins // 10 != 1: 'монеты',
            coins % 10 == 0: 'монет',
        }[True]

myCoins = Parameters()
coins = 1
print(myCoins.showCoins())
coins = 10
print(myCoins.showCoins())
coins = 3
print(myCoins.showCoins())