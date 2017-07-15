# Given a binary tree, return the zigzag level order traversal of its nodes’ values. (ie, from left to right, then right to left for the next level and alternate between).

# Example : 
# Given binary tree

#     3
#    / \
#   9  20
#     /  \
#    15   7
# return

# [
#          [3],
#          [20, 9],
#          [15, 7]
# ]

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def zigZag(self, root):
	ret = []
	level = 1
	if root is None:
		return []
	ret.append(root.val)
	