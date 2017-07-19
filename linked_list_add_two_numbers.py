# You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8

#     342 + 465 = 807
# Make sure there are no trailing zeros in the output list
# So, 7 -> 0 -> 8 -> 0 is not a valid response even though the value is still 807.

# SAMPLE SOLUTION (more elegant than mine)
# class Solution:
#     # @param A : head node of linked list
#     # @param B : head node of linked list
#     # @return the head node in the linked list
#     def addTwoNumbers(self, A, B):
#         a, b = A, B
#         head = ListNode(0)
#         cur_sum = head
#         while a != None or b != None or cur_sum.val > 9:
#             carry = cur_sum.val / 10
#             cur_sum.val %= 10
#             a_val = 0 if a == None else a.val
#             b_val = 0 if b == None else b.val
#             next_val = a_val + b_val + carry
#             cur_sum.next = ListNode(next_val)
#             cur_sum = cur_sum.next
#             a = None if a == None else a.next
#             b = None if b == None else b.next
#         return head.next

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def addTwoNumbers(self, A, B):
    	head = ListNode(0)
    	prev = ListNode(0)
    	first = True
    	carry_over = False
    	while A is not None and B is not None:
    		new = ListNode(0)
    		tmp = A.val + B.val
    		if carry_over:
    			tmp += 1
    			carry_over = False
    		if tmp >= 10:
    			tmp = tmp % 10
    			carry_over = True
    		if first:
    			head.val = tmp
    			prev = head
    			first = False
    		else:
    			new.val = tmp
    			prev.next = new
    			prev = new
    		A = A.next
    		B = B.next
    	if A is None:
    		while B is not None:
    			if carry_over:
    				B.val = B.val + 1
    				carry_over = False
    			if B.val >= 10:
    				B.val = B.val % 10
    				carry_over = True
    			prev.next = B
    			prev = B
    			B = B.next
    	elif B is None:
    		while A is not None:
    			if carry_over:
    				A.val = A.val + 1
    				carry_over = False
    			if A.val >= 10:
    				A.val = A.val % 10
    				carry_over = True
    			prev.next = A
    			prev = A
    			A = A.next
    	# for last carry over
    	if carry_over:
    		prev.next = ListNode(1)
    	# remove trailing zeroes
    	return head

# TEST
A = ListNode(1)
B = ListNode(9)
b2 = ListNode(9)
B.next = b2
b3 = ListNode(9)
b2.next = b3

C = ListNode(2)
c2 = ListNode(4)
C.next = c2
c3 = ListNode(3)
c2.next = c3

D = ListNode(5)
d2 = ListNode(6)
D.next = d2
d3 = ListNode(4)
d2.next = d3

s = Solution()
# head = s.addTwoNumbers(A, B)
head = s.addTwoNumbers(C, D)
while head is not None:
	print head.val
	head = head.next