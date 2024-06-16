#!/usr/bin/python3
"""
Rotate 2D Matrix module
"""

def rotate_2d_matrix(matrix):
    """
    Rotate the matrix 90 degrees clockwise in-place
    """
    if not matrix:
        return
    n = len(matrix)
    
    # Transpose the matrix
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Reverse each row
    for row in matrix:
        if row:
            row.reverse()

# End of code
