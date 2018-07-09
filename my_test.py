from recursion import*

def test_div():
    for x in range(-900, 900):
        for y in range(-900, 900):
            if y == 0:
                #print(x, "Value Error")
                continue
            elif div(x, y) != (x//y):
                print(x, "div ", y, "=", div(x, y))
                print(x, " // ", y, "=", x // y)


def test_exp():
    for x in range(-5, 6):
        for y in range(0, 6):
            if exp(x, y) != x ** y:
                print(x, "exp", y, "=", exp(x, y))
                print(x, "** ", y, "=", x ** y) 



