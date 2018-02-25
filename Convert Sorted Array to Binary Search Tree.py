import unittest
import TreeSolution

class TreeNode(object):
    def __init__(self, x = None):
        self.val = x
        self.left = None
        self.right = None

class unitest(unittest.TestCase):
    def testNone(self):
        Input = []
        Output = None
        self.assertEqual(Solution().sortedArrayToBST(Input),Output)
    def testSample(self):
        Input = [-10,-3,0,5,9]
        Output = Solution().sortedArrayToBST(Input)
        tree = TreeSolution.TreeSolution()
        Ans = [0,-3,9,-10,None,5]
        tree.checkAns(Output,Ans)

class Solution():
    def sortedArrayToBST(self, nums):
        if not nums:
            return None
        mid = int(len(nums)/2)
        node = TreeNode(nums[mid])
        node.left = self.sortedArrayToBST(nums[:mid])
        node.right = self.sortedArrayToBST(nums[mid+1:])
        return node

if __name__ == '__main__':
    unittest.main()
