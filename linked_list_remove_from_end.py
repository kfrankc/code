# Given a linked list, remove the nth node from the end of list and return its head.

# For example,
# Given linked list: 1->2->3->4->5, and n = 2.
# After removing the second node from the end, the linked list becomes 1->2->3->5.

# Note:
# * If n is greater than the size of the list, remove the first node of the list.
# Try doing it using constant additional space.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
	def removeNthFromEnd(self, head, n):
		tmp = head
		size = 1
		if tmp is None:
			return None
		elif tmp.next is None and n is 0:
			return tmp
		elif tmp.next is None and n > 0:
			return None
		else:
			while tmp.next is not None:
				tmp = tmp.next
				size += 1
			if (n > size) or (n == size):
				tmp3 = head.next
				return tmp3
			else:
				size_remaining = size - n
				tmp2 = head
				prev = head
				advance = False
				while size_remaining > 0:
					tmp2 = tmp2.next
					size_remaining -= 1
					if advance:
						prev = prev.next
					advance = True
				# perform deletion
				prev.next = tmp2.next
			return head

# TEST
list = ListNode(1)
l2 = ListNode(2)
list.next = l2
l3 = ListNode(3)
l2.next = l3
l4 = ListNode(4)
l3.next = l4
l5 = ListNode(5)
l4.next = l5
s = Solution()
head = s.removeNthFromEnd(list, 7)
while head is not None:
	print head.val
	head = head.next


