# Longest Common Subsequence

# The LCS of groups A and B is the longest group of elements from A and B that are common between the two groups
# and in the same order in each group.

# Example: "1234" and "1224533324" have an LCS of "1234"
# "thisisatest" and "testing123testing" would return "tsitest"

# Write a function which returns an LCS of two strings (case-sensitive). No need to show multiple LCS's.

class Solution():
	def lcs(self, A, B):
		strlens = [[0 for j in range(len(B)+1)] for i in range(len(A)+1)]
		for i, x in enumerate(A):
			for j, y in enumerate(B):
				if x == y:
					strlens[i+1][j+1] = strlens[i][j] + 1
				else:
					strlens[i+1][j+1] = max(strlens[i+1][j], strlens[i][j+1])
		ret = ""
		x = len(A)
		y = len(B)
		while x != 0 and y != 0:
			if strlens[x][y] == strlens[x-1][y]:
				x -= 1
			elif strlens[x][y] == strlens[x][y-1]:
				y -= 1
			else:
				ret = A[x-1] + ret
				x -= 1
				y -= 1
		return ret

# TEST
s = Solution()
A = "1234"
B = "1223533324"
C = "thisisatest"
D = "testing123testing"
print s.lcs(A, B) # print "1234"
print s.lcs(C, D) # print "tsitest"