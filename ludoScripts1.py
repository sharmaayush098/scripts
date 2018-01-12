import random


def players():
    n = input(print("How many players want to play"))
    try:
        if 1 < int(n) <= 4:
            print("Start Game with %s Players" % n)
        else:
            print("Wrong Input,Minimum 2 and Maximum 4 players can play")

    except ValueError:
        print("please enter the numeric values")


def moves_for_coins():
    list(range(1, 58))


def dice_number():
    number = list(range(1, 7))
    print(random.choice(number))


def coins():
    coin_1 = 0
    coin_2 = 0
    coin_3 = 0
    coin_4 = 0

    for number in list(range(1, 7)):
        print(random.choice(number))
        coin_1 += number
        coin_2 += number
        coin_3 += number
        coin_4 += number


def safe_postions():
    return [0, 8, 13, 21, 26, 34, 39, 47]
