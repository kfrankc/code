# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

# Note: You can only move either down or right at any point in time.
# Example :

# Input : 

#     [  1 3 2
#        4 3 1
#        5 6 1
#     ]

# Output : 8
#      1 -> 3 -> 2 -> 1 -> 1

# Notes: this probably requires memoization for efficiency. Use DP

class Solution:
    # @param A : list of list of integers
    # @return an integer
    def minPathSum(self, A):
    	R = len(A)
    	C = len(A[0])
    	costarr = [[0 for x in range(C)] for x in range(R)]
    	costarr[0][0] = A[0][0]

    	# Initialize first column of total cost (costarr) array
    	for i in range(1, R):
    		costarr[i][0] = costarr[i-1][0] + A[i][0]

    	# Initialize first row of costarr array
    	for j in range(1, C):
    		costarr[0][j] = costarr[0][j-1] + A[0][j]

    	# Construct rest of costarr array
    	for i in range(1, R):
    		for j in range(1, C):
    			costarr[i][j] = min(costarr[i-1][j], costarr[i][j-1]) + A[i][j]
    			# print "(%i, %i): %i" %(i, j, costarr[i][j])
    	return costarr[R-1][C-1]

# TEST
A = [[1, 3, 2],
	 [4, 3, 1],
	 [5, 6, 1]]
s = Solution();
print s.minPathSum(A)  # should print 8
