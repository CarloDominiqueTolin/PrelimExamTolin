import unittest

def if_happy(x):
    return x

class happy_test(unittest.TestCase):
    def test_if_happy(self):
        '''Checks if the function returns "HAPPY"'''
        #self.assertEqual(if_happy('HAPPY'),'HAPPY')    #<=OK
        self.assertEqual(if_happy('SAD'),'HAPPY')      #<=FAIL


if __name__ == "__main__":
    unittest.main()