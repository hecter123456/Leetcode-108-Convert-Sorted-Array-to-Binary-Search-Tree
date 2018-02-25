import unittest

class unitest(unittest.TestCase):
    def testNone(self):
        Input = None
        Output = None
        self.assertEqual(Solution().test(Input),Output)

class Solution():
    def test(self):
        return None

if __name__ == '__main__':
    unittest.main()
