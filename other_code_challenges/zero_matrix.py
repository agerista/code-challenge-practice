def zero_matrix(matrix):
    """Given an NxM matrix, find cells that equal zero, set their row and column to zeroes."""

    number_of_columns = len(matrix[0])
    number_of_rows = len(matrix)

    # Set a list for rows and columns so we know which rows/columns to clear
    columns = number_of_columns * [False]
    rows = number_of_rows * [False]

    if matrix == []:
        return []

    # Find zeros and set them to true in our lists
    for y in range(0, number_of_columns):
        for x in range(0, number_of_rows):

            if matrix[x][y] == 0:
                rows[x] = True
                columns[y] = True

    # Change appropriate rows and columns to zero
    for y in range(0, number_of_columns):
        for x in range(0, number_of_rows):

            if rows[x] or columns[y]:
                matrix[x][y] = 0

    return matrix

assert zero_matrix([['A', 'B', 'C', 'D'], ['E', 'F', 0, 'H'],
                    ['I', 'J', 'K', 'L']]) == [['A', 'B', 0, 'D'], [0, 0, 0, 0], ['I', 'J', 0, 'L']]
assert zero_matrix([[0, 1, 2, 3, 4, 5], [6, 7, 8, 9, 10, 11], [12, 13, 14, 15, 16, 17],
                    [18, 19, 20, 21, 22, 23]]) == [[0, 0, 0, 0, 0, 0], [0, 7, 8, 9, 10, 11], [0, 13, 14, 15, 16, 17], [0, 19, 20, 21, 22, 23]]
