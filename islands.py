def islands(input_matrix, threshold=5, minimum_island_size=3):
    """This Python function searches a given input_matrix for contiguous
    regions of values greater than the given threshold with some
    minimum_island_size.

    Args:
        input_matrix: the matrix to be searched for islands
        threshold: the minimum value which can be considered part of an
            island (default 5)
        minimum_island_size: minimum size of an island to be included in
            the output (default 3)

    Returns:
        A binary matrix showing the location of islands meeting the
        criteria of the arguments.
    """
    def map_island(row, column):
        """Check every location adjacent to the given[row][column].
        Update the island map and size if the location has a value
        greater than the threshold.
        Repeat for every location found above the threshold.
        """
        nonlocal island_size
        nonlocal number_checked_around
        nonlocal island_map
        if column < number_of_columns - 1:  # check right
            if not island_map[row][column + 1]:
                if input_matrix[row][column + 1] >= threshold:
                    island_size += 1
                    island_map[row][column + 1] = 1
                    map_island(row, column + 1)
        if column > 0:  # check left
            if not island_map[row][column - 1]:
                if input_matrix[row][column - 1] >= threshold:
                    island_size += 1
                    island_map[row][column - 1] = 1
                    map_island(row, column - 1)
        if row < number_of_rows - 1:  # check down
            if not island_map[row + 1][column]:
                if input_matrix[row + 1][column] >= threshold:
                    island_size += 1
                    island_map[row + 1][column] = 1
                    map_island(row + 1, column)
        if row > 0:  # check up
            if not island_map[row - 1][column]:
                if input_matrix[row - 1][column] >= threshold:
                    island_size += 1
                    island_map[row - 1][column] = 1
                    map_island(row, column)
        number_checked_around += 1

    def check_island(row, column):
        """Check if the island is large enough.
        Update the output_matrix if it is.
        """
        nonlocal island_size
        nonlocal number_checked_around
        nonlocal island_map
        nonlocal output_matrix
        island_size = 1
        island_map[row][column] = 1
        number_checked_around = 0
        map_island(row, column)
        for r in range(number_of_rows):
            for c in range(number_of_columns):
                if island_size > minimum_island_size:
                    output_matrix[r][c] = island_map[r][c]
                else:
                    island_map[r][c] = output_matrix[r][c]
    number_of_rows = len(input_matrix)
    number_of_columns = len(input_matrix[0])
    output_matrix = [0] * number_of_rows
    island_map = [0] * number_of_rows
    island_size = 0
    number_checked_around = 0
    for rows in range(number_of_rows):
        output_matrix[rows] = [0] * number_of_columns
        island_map[rows] = [0] * number_of_columns
    for rows in range(number_of_rows):
        for columns in range(number_of_columns):
            if output_matrix[rows][columns]:
                continue
            if input_matrix[rows][columns] < threshold:
                continue
            check_island(rows, columns)
    return output_matrix
