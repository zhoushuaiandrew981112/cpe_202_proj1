# Name:          Zhoushuai(Andrew) Wu
# Course:        CPE 202
# Instructor:    Daniel Kauffman
# Assignment:    Proj 1: Recursion
# Term:          Summer 2018

import ctypes


def main():
    pass


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
    if x == 0 or y == 0:                         # Base Case: If one of the input is zero
        return 0                                 # return zero
    elif y < x:                                  # If y is less than x, pass in x and y in swapped order
        return mul(y, x)                         # call mul with swap x and y. (to avoid case y<0 and x>0)
    elif y < 0 and x < 0:                        # both x and y are neg, product is positive
        return mul(abs(x), abs(y))               # call mul with magnitude of x and y passed in
    elif y > 0:                                  # if y is greater, produc is sum of x, no sign change
        return x + mul(x, sub(abs(y), 1))        # call mul to add returned x while decreasing magitude of y


def exp(x, y):
    if y < 0:				    # if y is less than zero, not in domain of this operation
        raise ValueError		    # raise value error
    elif y == 0:                            # Base case: if y is zero
        if x == 0:                          # is raise zero to zero power
            return 0			    # return zero in scope of this function operation
        else:                               # if any other integer
            return 1                        # return 1
    else:                                   # if normal case
        return mul(x, exp(x, sub(y, 1)))    # return pruduct of x and the returned value of next mul


def div(x, y):
    if y == 0:                                       # if y is equal to zero, operation input error
        raise ValueError                             # raise ValueError 
    elif abs(x) < abs(y):                            # Base case: if the magnitude of dividend is less than divisor 
        return 0                                     # end of division, return zero
    elif x > 0 and y < 0 or x < 0 and y > 0:         # if two input has sign difference, quotient is negative
        return add(sub(0, 1), div(add(x, y), y))     # return -1 plus return value of next div func
    else:                                            # if sign of dividend and divisor are same
        return 1 + div(sub(abs(x), abs(y)), abs(y))  # return 1 plus return value of next div func


def mod(x, y):
    radix = 10
    if y == 0:
        raise ValueError
    elif x == y:
        return 0
    elif x > 0 and y > 0 or x < 0 and y < 0:
        if abs(x) < abs(y):
            return x
        elif abs(x) > abs(y):
            return mod(sub(x, y), y)
    elif x < 0 and y > 0:
        if abs(x) < y:
            return add(x, y)
        elif abs(x) > y:
            return mod(add(x, y), y)
    elif x > 0 and y < 0:
        if x < abs(y):
            return add(x, y)
        elif x > abs(y):
            return mod(add(x, y), y)





if __name__ == "__main__":
    main()



