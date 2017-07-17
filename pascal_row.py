# Given an index k, return the kth row of the Pascal's triangle.

# Pascal's triangle : To generate A[C] in row R, sum up A'[C] and A'[C-1] from previous row R - 1.

# Example:

# Input : k = 3

# Return : [1,3,3,1]
# NOTE : k is 0 based. k = 0, corresponds to the row [1].
# Note: Could you optimize your algorithm to use only O(k) extra space?

class Solution:
	def pascalRow(self, k):
		k += 1
		rowMatrix = [[1]]
		if k == 0:
			return rowMatrix[0]
		for row in range(2, k+1):
			rowMatrix.append([0]*row)
			rowMatrix[row-1][0] = 1
			rowMatrix[row-1][-1] = 1
			for col in range(1, row-1):
				rowMatrix[row-1][col] = rowMatrix[row-2][col-1] + rowMatrix[row-2][col]
		return rowMatrix[k-1]

# TEST
S = Solution()
print S.pascalRow(2)
print S.pascalRow(6)