# Reverse digits of an integer.

# Example1:

# x = 123,

# return 321
# Example2:

# x = -123,

# return -321

# Return 0 if the result overflows and does not fit in a 32 bit signed integer

def reverse(n):
	nstr = str(n)
	if nstr[0] == '-':
		new_str = nstr[1:]
		new_str = new_str[::-1]
		new_str = '-' + new_str
		if (int(new_str) > 2147483647) or (int(new_str) < -2147483648):
		    return 0
		return int(new_str)
	else:
		return int(nstr[::-1])

# TEST

print reverseDigit(123)
print reverseDigit(-123)
print reverseDigit(100)