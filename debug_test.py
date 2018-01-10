
def func(a, b, c):
    if a > b:
        if a > c:
            print(a)
        else:
            print(c)
    elif b > c:
        print(b)
    else:
        print(c)


func(23, 56, 88)