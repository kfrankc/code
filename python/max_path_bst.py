# Given a binary tree, find the maximum path sum.

# The path may start and end at any node in the tree.

# Example :

# Given the below binary tree,

#        1
#       / \
#      2   3
#
# Return 6.

# Notes: in a binary search tree, we want to start from the right-most leaf node left of the root
# then to the root, then move right until we reach the right-most leaf node right of the root

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param Root : root node of tree
    # @return an integer
    def maxPathSum(self, Root):
    	# traverse left
    	left = Root.left
    	left_sum = 0
    	while left is not None:
    		left_sum += left.val
    		if left.right is None:
    			left = left.left
    		else:
    			left = left.right
    	# traverse right
    	right = Root.right
    	right_sum = 0
    	while right is not None:
    		right_sum += right.val
    		if right.right is None:
    			right = right.left
    		else:
    			right = right.right
    	return right_sum + left_sum + Root.val


# TEST (only for binary search trees)
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
