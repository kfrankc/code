# Given an integer n, return the number of trailing zeroes in n!.

# Note: Your solution should be in logarithmic time complexity.

# Example :

# n = 5
# n! = 120 
# Number of trailing zeros = 1
# So, return 1

# n = 3, n! = 6, trailing_zeroes(n) = 0
# n = 10, n! = 3628800, trailing_zeroes(n) = 2

def trailingZeroes(n):
	ret = 0
	while n != 0:
		ret = ret + (n / 5)
		n = n / 5
	return ret

# TEST
n = 9247
print trailingZeroes(n)

