class Node:
	def __init__(self, key):
		self.rc = None
		self.lc = None
		self.data = key

def bst_insert(root, node):
	if root is None:
		root = node
	else:
		if root.data > node.data:
			if root.lc is None:
				root.lc = node
			else:
				bst_insert(root.lc, node)
		else:
			if root.rc is None:
				root.rc = node
			else:
				bst_insert(root.rc, node)

def in_order_print(root):
	if not root:
		return
	in_order_print(root.lc)
	print root.data
	in_order_print(root.rc)

def pre_order_print(root):
	if not root:
		return
	print root.data
	pre_order_print(root.lc)
	pre_order_print(root.rc)

# TEST
r = Node(10)
bst_insert(r, Node(15))
bst_insert(r, Node(5))
bst_insert(r, Node(1))
bst_insert(r, Node(3))

in_order_print(r)
pre_order_print(r)
