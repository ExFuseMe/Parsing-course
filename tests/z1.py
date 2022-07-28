import unittest

class Test1(unittest.TestCase):

    def test_test1(self):
        total = 5*5
        self.assertEqual(25, total)



if __name__ == '__main__':
    unittest.main()