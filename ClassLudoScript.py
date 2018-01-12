import random


class Players():
    def __init__(self, path):
        self.path = path

    def number(self, random_number):
        self.random_number = random_number
        return random_number

    def coins(self, coin1, coin2, coin3, coin4):
        self.coin_1 = coin1
        self.coin_2 = coin2
        self.coin_3 = coin3
        self.coin_4 = coin4

        for self.random_number in self.path:
            self.coin_1 += self.random_number

lists = Players(list(range(1, 58)))
num = lists.number(random.choice(list(range(1, 7))))







