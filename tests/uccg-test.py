'''Tu będą testy'''

import sys
sys.path.append('../uccg-main-unit')
import main
import unittest

class TestStringMethods(unittest.TestCase):

    def test_init(self):
        self.assertTrue(main.init)


if __name__ == '__main__':
    unittest.main()
