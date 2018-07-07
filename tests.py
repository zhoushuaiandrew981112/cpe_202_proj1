from recursion import *
import unittest

class TestRecursion(unittest.TestCase):

    """ Test mul(x, y) """

    def test_mul_pos_and_pos(self):         # test positive multiply by positive
        self.assertEqual(mul(2, 3), 6)

    def test_mul_pos_and_neg(self):         # test positive multiply by negative
        self.assertEqual(mul(2, -3), -6)

    def test_mul_neg_and_pos(self):         # test negative multiply by positive
        self.assertEqual(mul(-2, 3), -6)

    def test_mul_neg_and_neg(self):         # test negative multiply by positive
        self.assertEqual(mul(-2, -3), 6)

    def test_mul_contain_zero(self):        # test when one of the argument is zero
        self.assertEqual(mul(0, 6), 0)      # zero multiply positive int
        self.assertEqual(mul(0, -6), 0)     # zero multiply negative int
        self.assertEqual(mul(6, 0), 0)      # positive int multiply zero
        self.assertEqual(mul(-6, 0), 0)     # negative int multiply zero
        self.assertEqual(mul(0, 0), 0)      # zero multiply zero


    """ Test exp(x, y) """    

    def test_exp_ValueError(self):           # test raising ValueError when power is negative
        with self.assertRaises(ValueError):
            exp(2, -1)

    def test_exp_zero_to_zero(self):         # test zero to zero power
        self.assertEqual(exp(0, 0), 0)

    def test_exp_int_to_zero(self):          # test int to zero power
        self.assertEqual(exp(100, 0), 1)     # test positive int to zero power
        self.assertEqual(exp(-100, 0), 1)    # test negative int to zero power

    def test_exp_int_to_int_01(self):        # test int to int power, 1's
        self.assertEqual(exp(1, 1), 1)       # test positive int to positive int power
        self.assertEqual(exp(-1, 1), -1)     # test negative int to positive int power

    def test_exp_int_to_int_02(self):        # test int to int power, 1 to int power other than 1
        self.assertEqual(exp(1, 2), 1)       # test positive int to even power equals positive int
        self.assertEqual(exp(-1, 2), 1)      # test negative int to even power equals positive int
        self.assertEqual(exp(1, 3), 1)       # test negative int to odd  power equals positive int
        self.assertEqual(exp(-1, 3), -1)     # test negative int to odd  power equals negative int

    def test_exp_int_to_int_03(self):        # test int to int power, non 1
        self.assertEqual(exp(2, 2), 4)       # test positive int to even power equals positive int
        self.assertEqual(exp(-2, 2), 4)      # test negative int to even power equals positive int
        self.assertEqual(exp(2, 3), 8)       # test positive int to odd  power equals positive int
        self.assertEqual(exp(-2, 3), -8)     # test negative int to odd  power equals negative int
        

    def test_exp_int_to_int_04(self):        # test bigger numbers to small power, non 1 power
        self.assertEqual(exp(10, 2), 100)    # test positive int to even power equals positive int
        self.assertEqual(exp(-10, 2), 100)   # test negative int to even power equals positive int
        self.assertEqual(exp(-10, 3), -1000) # test negative int to odd  power equals negative int
        self.assertEqual(exp(-10, 3), -1000) # test negative int to odd  power equals negative int

    def test_exp_int_to_int_05(self):        # test small numbers to bigger power, non 1 power
        self.assertEqual(exp(2, 10), 1024)   # test positive in to even power equals positive int 
        self.assertEqual(exp(-2, 10), 1024)  # test negative in to even power equals positive int 
        self.assertEqual(exp(2, 9), 512)     # test positive in to odd  power equals positive int 
        self.assertEqual(exp(-2, 9), -512)   # test negative in to odd  power equals negative int 


    """ Test div(x, y) """

    def test_div_by_zero(self):               # test division by zero, ValueError
        with self.assertRaises(ValueError):   # should raise ValueEVrror
            div(0, 0)                         # divide zero by zero
        with self.assertRaises(ValueError):   # should raise ValueEVrror
            div(2, 0)                         # divide positive int by zero
        with self.assertRaises(ValueError):   # should raise ValueEVrror
            div(-2, 0)                        # divide negative int zero by zero

    def test_div_by_one_even(self):           # test even int division by one
        self.assertEqual(div(2, 1), 2)        # test positive even int by positive one equal positive
        self.assertEqual(div(-2, 1), -2)      # test negative even int by positive one equal negative
        self.assertEqual(div(2, -1), -2)      # test positive even int by negative one equal negative 
        self.assertEqual(div(-2, -1), 2)      # test negative even int by negative one equal positive

    def test_div_by_one_odd(self):            # test odd  int division by one
        self.assertEqual(div(3, 1), 3)        # test positive odd  int by positive one equal positive
        self.assertEqual(div(-3, 1), -3)      # test negative odd  int by positive one equal negative
        self.assertEqual(div(3, -1), -3)      # test positive odd  int by negative one equal negative
        self.assertEqual(div(-3, -1), 3)      # test negative odd  int by negative one equal positive

    def test_div_no_remain_even(self):        # test even int division by even int, no remainder
        self.assertEqual(div(10, 2), 5)       # test positive even int division by even int equal positive
        self.assertEqual(div(-10, 2), -5)     # test positive even int division by even int equal negative
        self.assertEqual(div(10, -2), -5)     # test positive even int division by even int equal negative 
        self.assertEqual(div(-10, -2), 5)     # test positive even int division by even int equal positive
    
    def test_div_no_remain_odd(self):         # test even int division by even int, no remainder
        self.assertEqual(div(15, 3), 5)       # test positive even int division by even int equal positive
        self.assertEqual(div(-15, 3), -5)     # test positive even int division by even int equal negative
        self.assertEqual(div(15, -3), -5)     # test positive even int division by even int equal negative 
        self.assertEqual(div(-15, -3), 5)     # test positive even int division by even int equal positive

    def test_div_x_less_than_y(self):         # test when smaller int is dividing bigger int
        self.assertEqual(div(3, 4), 0)        # test positive int div positive int
        self.assertEqual(div(-3, 4), 0)       # test negative int div negative int
        self.assertEqual(div(3, -4), 0)       # test positive int div positive int
        self.assertEqual(div(-3, -4), 0)      # test negative int div negative int

    def test_div_with_remain(self):           # test when the division has remainder
        self.assertEqual(div(8, 3), 2)        # test positive int div positive int equal positive
        self.assertEqual(div(-8, 3), -2)      # test negative int div negative int equal negative
        self.assertEqual(div(8, -3), -2)      # test positive int div positive int equal negative
        self.assertEqual(div(-8, -3), 2)      # test negative int div negative int equal positive


if __name__ == '__main__':
    unittest.main()

