def case1():
    print("you loose,better luck next time")
def case2():
    print("move to 2nd  step")
def case3():
    print("move to 3rd step")
def case4():
    print("move to 4th step")
def case5():
    print("you won congratulations")
def case6():
    print("you loose,at last step.")

choice = {1: case1, 2: case2, 3: case3, 4: case4,
          5: case5,6:case6 }
def start():
    print("""let us play a game . choose the right number to win.choose 1 or 2 """)
    number = input()
    if int(number) == 2:
        choice[2]()
        print("now ,choose any one number from 3 or 4")
        number = input()
        if int(number) == 3:
            choice[3]()
            print("keep going ,you are on right choice,now choose number from 5 or 6")
            number = input()
            if int(number) == 5:
                choice[5]()
            else:
                choice[6]()

        else:
            choice[1]()


    else:
        choice[1]()
start()


