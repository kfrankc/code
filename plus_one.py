# Given a non-negative number represented as an array of digits,

# add 1 to the number ( increment the number represented by the digits ).

# The digits are stored such that the most significant digit is at the head of the list.

# Example:

# If the vector has [1, 2, 3]

# the returned vector should be [1, 2, 4]

# as 123 + 1 = 124.

# Notes: my solution was done in a hurry, and did not satisfy some complexity requirements.
# Here is complete solution:
# class Solution:
#     # @param A : list of integers
#     # @return a list of integers
#     def plusOne(self, A):
#         A[-1] += 1
#         temp = 0
#         tempSum = 0
#         for i in range(len(A)-1,-1,-1):
#     	    tempSum = A[i]+temp
#     	    temp = (A[i]+temp)/10
#     	    A[i] = tempSum%10
#         if temp > 0:
#     	    A = [temp] + A
#         i = 0
#         while i < len(A):
#             if A[i] > 0:
#                 break
#             i += 1
#         return A[i:]

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
    	Ar = A[::-1]
    	carry_over = False
    	first = True
    	for idx, val in enumerate(Ar):
			if carry_over:
				val = val + 1
				Ar[idx] = val
				carry_over = False
				# for appending to end of list
				if val >= 10 and idx is len(Ar)-1:
					val = val % 10
					Ar[idx] = val
					Ar.append(1)
				elif val >= 10:
					val = val % 10
					Ar[idx] = val
					carry_over = True
			if first:
				val = val + 1
				Ar[idx] = val
				if val >= 10 and idx is len(Ar)-1:
					val = val % 10
					Ar[idx] = val
					Ar.append(1)
				elif val >= 10:
					val = val % 10
					Ar[idx] = val
					carry_over = True
				first = False
	# remove leading zeros
	A = Ar[::-1]
	i = 0
	while i < len(A):
		if A[i] > 0:
			break
		i += 1
	return A[i:]


# TEST
A = [1, 2, 3]
B = [9, 9, 9]
C = [1, 9, 9, 9, 9, 9, 9]
D = [6, 4, 7, 7, 8, 9]
E = [0, 3, 7, 6, 4, 0, 5, 5, 5]
F = [0, 6, 0, 6, 4, 8, 8, 1]
G = [9]
s = Solution()
print s.plusOne(A) # should return [1, 2, 4]
print s.plusOne(B) # should return [1, 0, 0, 0]
print s.plusOne(C) # should return [2, 0, 0, 0, 0, 0, 0]
print s.plusOne(D) # should return [6, 4, 7, 7, 9, 0]
print s.plusOne(E) # should return [3, 7, 6, 4, 0, 5, 5, 6]
print s.plusOne(F) # should return [6, 0, 6, 4, 8, 8, 2]
print s.plusOne(G) # should return [1, 0]