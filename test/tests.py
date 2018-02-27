import unittest

import ledCheck.light as l

from testfunc import test_grids

class TestLights(unittest.TestCase):
            
    def test_1(self):
        self.assertEqual(test_grids(5), 25)
        self.assertEqual(test_grids(100), 100**2)
        self.assertEqual(test_grids(1), 1)
        self.assertEqual(test_grids(0), 0)
        self.assertEqual(test_grids(5), 5)
        self.assertEqual(test_grids(5), 5)
        

        
    def wrong_test(self):
        self.assertEqual(test_grids(5), 5)
        
    def mytest(self):
        self.assertFalse(True)        

if __name__ == '__main__':
    unittest.main()