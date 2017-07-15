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

class Solution:
	def update(self, node, level):
		while len(self.levels) < level:
			self.levels.append([])
		self.levels[level-1].append(node.val)

	def traverse(self, node, level):
		if node is None:
			return 
		self.traverse(node.right, level+1)
		self.traverse(node.left, level+1)
		self.update(node, level)

	def zigZag(self, root):
		self.levels = []
		self.traverse(root, 1)

		for i, level in enumerate(self.levels):
			if i % 2 == 0:
				self.levels[i] = levels[::-1]

		return self.levels
	
