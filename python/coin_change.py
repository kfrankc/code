# Coin Change - Dynamic Programming

class Solution:
	# vals: array containing value of the coins
	# total: total to give back
	# returns: minimal number of coins to make a total of t
	def coinChange(self, vals, t):
		tmparr = [0 for i in range(0, t+1)]
		n = len(vals)
		for i in range(1, t+1):
			minimum = float("inf")
			for j in range(0, n):
				if (vals[j] <= i):
					minimum = min(minimum, tmparr[i-vals[j]])
			tmparr[i] = 1 + minimum
		return tmparr[t]

# TEST
s = Solution()
vals = [1, 3, 4]
t = 20
print s.coinChange(vals, t) # print 5