# Given a column title as appears in an Excel sheet, return its corresponding column number.

# Example:

#     A -> 1
    
#     B -> 2
    
#     C -> 3
    
#     ...
    
#     Z -> 26
    
#     AA -> 27
    
#     AB -> 28 

def titleToNumber(col_title):
	length = len(col_title)
	col_title = col_title[::-1]
	number = 0
	for i in range(length):
		number += (26**(i)) * (ord(col_title[i]) - ord('A') + 1)
	return number

print titleToNumber('A')
print titleToNumber('AB')