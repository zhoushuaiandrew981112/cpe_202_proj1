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
        self.assertEqual(exp(0, 0), 1)

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
        self.assertEqual(div(-3, 4), -1)       # test negative int div negative int
        self.assertEqual(div(3, -4), -1)       # test positive int div positive int
        self.assertEqual(div(-3, -4), 0)      # test negative int div negative int

    def test_div_with_remain(self):           # test when the division has remainder
        self.assertEqual(div(8, 3), 2)        # test positive int div positive int equal positive
        self.assertEqual(div(-8, 3), -3)      # test negative int div negative int equal negative
        self.assertEqual(div(8, -3), -3)      # test positive int div positive int equal negative
        self.assertEqual(div(-8, -3), 2)      # test negative int div negative int equal positive


        """ mod(x, y) """

    def test_mod_ValueError(self):            # test raising ValueError
        with self.assertRaises(ValueError):    
            mod(0, 0)                         # zero mod zero
        with self.assertRaises(ValueError):
            mod(1, 0)                         # positive odd int mod zero
        with self.assertRaises(ValueError):
            mod(-1, 0)                        # negative odd int mod zero
        with self.assertRaises(ValueError):
            mod(2, 0)                         # positive even int mod zero
        with self.assertRaises(ValueError):
            mod(-2, 0)                        # negative even int mod zero

    def test_mod_zero_mod_int(self):          # test zero mod pos and neg int
        self.assertEqual(mod(0, 1), 0)
        self.assertEqual(mod(0, 2), 0)
        self.assertEqual(mod(0, 3), 0)
        self.assertEqual(mod(0, -1), 0)
        self.assertEqual(mod(0, -2), 0)
        self.assertEqual(mod(0, -3), 0)

    def test_mod_equal_inputs(self):          # test when both in puts are equal, remainder zero
        self.assertEqual(mod(1, 1), 0)        # test pos int mod pos int 
        self.assertEqual(mod(2, 2), 0) 
        self.assertEqual(mod(3, 3), 0)
        self.assertEqual(mod(-1, -1), 0)      # test neg int mod neg int 
        self.assertEqual(mod(-2, -2), 0)
        self.assertEqual(mod(-3, -3), 0) 

    def test_mod_signed_big_mod_small_even(self):  # test num with bigger magnitude mod num with smaller magnitude
        self.assertEqual(mod(6, 4), 2)             # pos even int mod pos even int
        self.assertEqual(mod(6, -4), -2)           # pos even int mod neg even int
        self.assertEqual(mod(-6, 4), 2)            # neg even int mod pos even int
        self.assertEqual(mod(-6, -4), -2)          # neg even int mod neg even int 
  
    def test_mod_signed_big_mod_small_odd(self):   # test num with bigger magnitude mod num with smaller magnitude
        self.assertEqual(mod(7, 3), 1)             # pos odd  int mod pos odd  int
        self.assertEqual(mod(7, -3), -2)           # pos odd  int mod neg odd  int
        self.assertEqual(mod(-7, 3), 2)            # neg odd  int mod pos odd  int
        self.assertEqual(mod(-7, -3), -1)          # neg odd  int mod neg odd  int 

    def test_mod_signed_small_mod_big_even(self):  # test mum with smaller magnitude mod num with bigger magnitude
        self.assertEqual(mod(4, 10), 4)            # pos even int mod pos even int
        self.assertEqual(mod(4, -10), -6)          # pos even int mod neg even int
        self.assertEqual(mod(-4, 10), 6)           # neg even int mod pos even int
        self.assertEqual(mod(-4, -10), -4)         # neg even int mod neg even int

    def test_mod_signed_small_mod_big_odd(self):   # test num with smaller magnitude mod num with bigger magnitude
        self.assertEqual(mod(5, 13), 5)            # pos odd  int mod pos odd  int
        self.assertEqual(mod(5, -13), -8)          # pos odd  int mod neg odd  int
        self.assertEqual(mod(-5, 13), 8)           # neg odd  int mod pos odd  int
        self.assertEqual(mod(-5, -13), -5)         # neg odd  int mod neg odd  int


    """ Test con """

    def test_con_base_2(self):         # Test convert from base 10 to base
        self.assertEqual(con(123, 2), "1111011")

    def test_con_base_3(self):         # Test convert from base 10 to base
        self.assertEqual(con(123, 3), "11120")

    def test_con_base_4(self):         # Test convert from base 10 to base
        self.assertEqual(con(123, 4), "1323")

    def test_con_base_5(self):         # Test convert from base 10 to base
        self.assertEqual(con(123, 5), "443")

    def test_con_base_6(self):         # Test convert from base 10 to base
        self.assertEqual(con(123, 6), "323")

    def test_con_base_7(self):         # Test convert from base 10 to base
        self.assertEqual(con(123, 7), "234")

    def test_con_base_8(self):         # Test convert from base 10 to base
        self.assertEqual(con(123, 8), "173")

    def test_con_base_9(self):         # Test convert from base 10 to base
        self.assertEqual(con(123, 9), "146")

    def test_con_base_10(self):         # Test convert from base 10 to base
        self.assertEqual(con(123, 10), "123")

    def test_con_base_11(self):         # Test convert from base 10 to base
        self.assertEqual(con(123, 11), "102")

    def test_con_base_12(self):         # Test convert from base 10 to base
        self.assertEqual(con(123, 12), "A3")

    def test_con_base_13(self):         # Test convert from base 10 to base
        self.assertEqual(con(123, 13), "96")

    def test_con_base_14(self):         # Test convert from base 10 to base
        self.assertEqual(con(123, 14), "8B")

    def test_con_base_15(self):         # Test convert from base 10 to base
        self.assertEqual(con(123, 15), "83")

    def test_con_base_16(self):         # Test convert from base 10 to base
        self.assertEqual(con(123, 16), "7B")


    """ Test fac(x, acc = 1) """
    def test_fac_ValueError(self):
        with self.assertRaises(ValueError):
            fac(-1)

    def test_fac_zero(self):
        self.assertEqual(fac(0), 1)

    def test_fac_1(self):
        self.assertEqual(fac(1), 1)

    def test_fac_2(self):
        self.assertEqual(fac(2), 2)
    
    def test_fac_3(self):
        self.assertEqual(fac(3), 6)

    def test_fac_4(self):
        self.assertEqual(fac(4), 24)

    def test_fac_5(self):
        self.assertEqual(fac(5), 120)

    def test_fac_6(self):
        self.assertEqual(fac(6), 720)


    """ Test fib(x, acc = (0, 1)) """
    
    def test_fib_0(self):
        self.assertEqual(fib(0), 0) 

    def test_fib_1(self):
        self.assertEqual(fib(1), 1)

    def test_fib_2(self):
        self.assertEqual(fib(2), 1)

    def test_fib_3(self):
        self.assertEqual(fib(3), 2)

    def test_fib_4(self):
        self.assertEqual(fib(4), 3)

    def test_fib_5(self):
        self.assertEqual(fib(5), 5)





if __name__ == '__main__':
    unittest.main()

