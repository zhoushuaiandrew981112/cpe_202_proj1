# Name:          Zhoushuai(Andrew) Wu
# Course:        CPE 202
# Instructor:    Daniel Kauffman
# Assignment:    Proj 1: Recursion
# Term:          Summer 2018

import ctypes


def main():
    input_str = input("> ")
    try:
        if input_str == "q":
            return
        input_list = input_str.split()
        for index in range(1, len(input_list)):
            input_list[index] = int(input_list[index])
        if input_list[0] == "add":
            print(add(input_list[1], input_list[2]))
        elif input_list[0] == "sub":
            print(sub(input_list[1], input_list[2]))
        elif input_list[0] == "mul":
            print(mul(input_list[1], input_list[2]))
        elif input_list[0] == "exp":
            print(exp(input_list[1], input_list[2]))
        elif input_list[0] == "div":
            print(div(input_list[1], input_list[2]))
        elif input_list[0] == "mod":
            print(mod(input_list[1], input_list[2]))
        elif input_list[0] == "con":
            print(con(input_list[1], input_list[2]))
        elif input_list[0] == "fac":
            print(fac(input_list[1]))
        elif input_list[0] == "fib":
            print(fib(input_list[1]))
    except:
        print("Error")
    print()
    main()


def add(x, y):
    if y == 0:
        return x
    carry = x & y
    cx = ctypes.c_int64(x ^ y)
    cy = ctypes.c_int64(carry << 1)
    return add(cx.value, cy.value)


def sub(x, y):
    return add(x, add(~y, 1))


def mul(x, y):
    if x == 0 or y == 0:
        return 0
    elif abs(x) < abs(y):
        return mul(y, x)
    elif x > 0 and y < 0:
        return add(sub(0, x), mul(x, add(y, 1)))
    elif x < 0 and y > 0:
        return add(x, mul(x, sub(y, 1)))
    elif x < 0 and y < 0 or x > 0 and y > 0:
        return add(abs(x), mul(abs(x), sub(abs(y), 1)))


def exp(x, y):
    if y < 0:				    # if y is less than zero, not in domain of this operation
        raise ValueError		    # raise value error
    elif y == 0:                            # Base case: if y is zero
        return 1
    else:                                   # if normal case
        return mul(x, exp(x, sub(y, 1)))    # return pruduct of x and the returned value of next mul


def div(x, y):
    if y == 0:                                       # if y is equal to zero, operation input error
        raise ValueError                             # raise ValueError 
    elif x > 0 and y < 0 or x < 0 and y > 0:         # if two input has sign difference, quotient is negative
        return add(sub(0, 1), div(add(x, y), y))     # return -1 plus return value of next div func
    elif abs(x) < abs(y):                            # Base case: if the magnitude of dividend is less than divisor 
        return 0                                     # end of division, return zero
    else:                                            # if sign of dividend and divisor are same
        return 1 + div(sub(abs(x), abs(y)), abs(y))  # return 1 plus return value of next div func


def mod(x, y):
    if y == 0:
        raise ValueError
    elif x >= 0 and y > 0 or x <= 0 and y < 0:
        if abs(x) < abs(y):
            return x
        elif abs(x) >= abs(y):
            return mod(sub(x, y), y)
    elif abs(x) <= abs(y):
        return add(x, y)
    elif abs(x) > abs(y):
        return mod(add(x, y), y)
   
 
def con(number, base):
    con_str = "0123456789ABCDEF" 
    if number < base:
        return con_str[number]
    else:
        return con(div(number, base), base) + con_str[mod(number, base)] 


def fac(x, acc = 1):
    if x < 0:
        raise ValueError
    elif x == 0:
        return acc
    else:
        return fac(sub(x, 1), mul(acc, x))


def fib(x, acc = (0, 1)):
    if x == 0:
        return acc[0]
    elif x == 1:
        return acc[1]
    else:
        return fib(sub(x, 1), (acc[1], add(acc[0], acc[1]))) 














if __name__ == "__main__":
    main()



