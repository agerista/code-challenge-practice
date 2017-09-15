def one_through_nine(lst):
	"""Checks if list includes numbers 1-9 inclusive"""

	final = set()

	if lst == []:
		return False

	if lst is None:
		return False

	for num in lst:
		if num in range(1, 10):
			final.add(num)

		else:
			return False

    
	if len(final) == 9:
		print lst, "valid"

	else:
		print lst, "invalid"

	return len(final) == 9

def valid_choice(num, lst):
	"""Check if the number is a valid choice"""

	if num >= 1 and num < 10:
		if num not in lst:
			return True

	return False

def correct_matrix(matrix):
	"""Checks rows, columns, squares to ensure all are valid choices"""

	column = []
	square = []
	i = 0

	for row in matrix:
		if not one_through_nine(row):
			return False
	print "rows are valid"
	for row in matrix:
		i = 0
		column = []
		while i < 9:
			column.append(row[i])
			i+=1

			if not one_through_nine(column):
				return False
	print "columns are valid"
	j = 0
	k = 0
	for j in [0, 3, 6]:
		for k in [0, 3, 6]:
			print j, k
			square = matrix[j][k:k + 3] + matrix[j + 1][k:k + 3] + matrix[j + 2][k:k + 3]
		
			if not one_through_nine(square):
				return False

	return True

		
assert correct_matrix([ [5, 3, 4, 6, 7, 8, 9, 1, 2],
  [6, 7, 2, 1, 9, 5, 3, 4, 8],
  [1, 9, 8, 3, 4, 2, 5, 6, 7],

  [8, 5, 9, 7, 6, 1, 4, 2, 3],
  [4, 2, 6, 8, 5, 3, 7, 9, 1],
  [7, 1, 3, 9, 2, 4, 8, 5, 6],

  [9, 6, 1, 5, 3, 7, 2, 8, 4],
  [2, 8, 7, 4, 1, 9, 6, 3, 5],
  [3, 4, 5, 2, 8, 6, 1, 7, 9]]) == True


# assert valid_choice(3, [3, 6]) == False
# assert valid_choice(10, [3, 6]) == False
# assert valid_choice(5, [3, 6]) == True

# assert one_through_nine([ ]) == False
# assert one_through_nine(None) == False
# assert one_through_nine([1, 2]) == False
# assert one_through_nine([1, 2, 3, 4, 5, 9, 7, 6, 8]) == True
# assert one_through_nine([-1]) == False
# assert one_through_nine([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == False
# assert one_through_nine([1, 1, 1, 1, 1, 1, 1, 1, 1]) == False
# assert one_through_nine([1, 2, 3, 4, 5, 6, 8, 9, 9]) == False