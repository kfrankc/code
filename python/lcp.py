# Write a function to find the longest common prefix string amongst an array of strings.
import sys

class Solution():
	def isCommonPrefix(self, strs, length):
		s = strs[0][0:length]
		for i in range(1, len(strs)):
			if strs[i].startswith(s) is False:
				return False
		return True

	def longestCommonPrefix(self, strs):
		if strs is [] or len(strs) is 0:
			return ""
		min_len = sys.maxint
		for s in strs:
			min_len = min(min_len, len(s))
		low = 1
		high = min_len
		while (low <= high):
			middle = (low + high) / 2
			if (self.isCommonPrefix(strs, middle)):
				low = middle + 1
			else:
				high = middle -1
		return strs[0][0:(low + high)/2]

# TEST
s = Solution()
strs = ["aba", "abb", "abc", "absolve"]
strs2 = ["leets", "leetcode", "leetc", "leeds"]
print s.longestCommonPrefix(strs) # print "ab"
print s.longestCommonPrefix(strs2) # print "lee"