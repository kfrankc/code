# Given numRows, generate the first numRows of Pascal's triangle.

# Pascal's triangle : To generate A[C] in row R, sum up A[C] and A'[C-1] from previous row R - 1.

# Example:

# Given numRows = 5,

# Return

# [
#      [1],
#      [1,1],
#      [1,2,1],
#      [1,3,3,1],
#      [1,4,6,4,1]
# ]

def pascalRows(numRows):
	rowMatrix = []
	if numRows == 0:
		return rowMatrix
	rowMatrix = [[1]]
	for row in range(2, numRows+1):
		rowMatrix.append([0]*row)
		rowMatrix[row-1][0] = 1
		rowMatrix[row-1][-1] = 1
		for col in range(1, row-1):
			rowMatrix[row-1][col] = rowMatrix[row-2][col-1] + rowMatrix[row-2][col]
	return rowMatrix

# TEST

print pascalRows(0)
print pascalRows(1)
print pascalRows(5)