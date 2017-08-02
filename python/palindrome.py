# Given a string s, partition s such that every substring of the partition is a palindrome.

# Return the minimum cuts needed for a palindrome partitioning of s.

# Example : 
# Given 
# s = "aab",
# Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.

# Approach: minCut is a dynamic programming question
# Create a 2D matrix of default-False, then set to True if A[i] and A[j] are the same character

# From http://www.geeksforgeeks.org/dynamic-programming-set-17-palindrome-partitioning/:
# i is the starting index and j is the ending index. i must be passed as 0 and j as n-1
# minPalPartion(str, i, j) = 0 if i == j. // When string is of length 1.
# minPalPartion(str, i, j) = 0 if str[i..j] is palindrome.

# If none of the above conditions is true, then minPalPartion(str, i, j) can be 
# calculated recursively using the following formula.
# minPalPartion(str, i, j) = Min { minPalPartion(str, i, k) + 1 +
#                                  minPalPartion(str, k+1, j) } 
#                            where k varies from i to j-1

class Solution:
    # @param A : string
    # @return an integer
    def minCut(self, A):
    	dp = [len(A) - i for i in range(len(A)+1)]
    	tmp = [[False for i in range(len(A))] for j in range(len(A))]
    	for i in range(len(A)-1, -1, -1):
    		for j in range(i, len(A)):
    			if A[i] == A[j] and (j - i < 2 or tmp[i+1][j-1]):
    				tmp[i][j] = True
    				dp[i] = min(dp[j+1] + 1, dp[i])
    	return dp[0] - 1

# TEST
A = "aab"
B = "ababbbabbababa"
s = Solution()
print s.minCut(A) # print 1
print s.minCut(B) # print 3
