def start():
    print("""let us play a game.\nIn this game you have three levels.
             After completing the three levels you will find Gold that is all yours.
              Let us start the game""")
    first_level()
def first_level():
    print("there are two doors which one will you choose? 1 or 2")
    a=input()
    if int(a)==2:
        print("congrats you are on right path")
    else:
        print("there is dragon out here.shit...you are dead")
start()


