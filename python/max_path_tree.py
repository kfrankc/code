# Given a binary tree, find the maximum path sum.

# The path may start and end at any node in the tree.

# Example :

# Given the below binary tree,

#        1
#       / \
#      2   3
#
# Return 6.

import sys

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # DP function
    def helper(self, Root, max_arr):
        if Root is None:
            return 0
        left = self.helper(Root.left, max_arr)
        right = self.helper(Root.right, max_arr)
        current = max(Root.val, max(Root.val + left, Root.val + right))
        max_arr[0] = max(max_arr[0], max(current, left + Root.val + right))
        return current

    # @param Root : root node of tree
    # @return an integer
    def maxPathSum(self, Root):
        max_arr = [-sys.maxint - 1]
        self.helper(Root, max_arr)
        return max_arr[0]


# TEST
#       4
#      / \
#     3   5
#    / \
#   1  2
# Return 2 + 3 + 4 + 5 = 14

root = TreeNode(4)
node = TreeNode(3)
root.left = node
root.right = TreeNode(5)
node.left = TreeNode(1)
node.right = TreeNode(2)
s = Solution()
print s.maxPathSum(root)
