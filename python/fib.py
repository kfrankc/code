# Given integer n, return the nth fibonacci number

# Note: fibonacci numbers: 1, 1, 2, 3, 5, 8, 13, 21, 34...

class Solution():
	def fib(self, n):
		fibVals = [0, 1]
		for i in range(2, n+1):
			fibVals.append(fibVals[i-1] + fibVals[i-2])
		return fibVals[n]

# TEST
s = Solution()
print s.fib(6) # print 5
print s.fib(20) # print 5