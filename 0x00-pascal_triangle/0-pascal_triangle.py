#!/usr/bin/python3

def pascal_triangle(num_rows):
    """
    Generates a Pascal's Triangle up to the given number of rows.

    Args:
    - num_rows: An integer representing the number of rows to generate.

    Returns:
    - A list of lists representing the Pascal's Triangle.
    """
    triangle = []
    for row_num in range(num_rows):
        row = [1] * (row_num + 1)
        if triangle:
            prev_row = triangle[-1]
            for i in range(1, row_num):
                row[i] = prev_row[i - 1] + prev_row[i]
        triangle.append(row)
    return triangle

# Test the function
result = pascal_triangle(5)
for row in result:
    print(row)

