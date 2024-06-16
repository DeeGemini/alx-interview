# Rotate 2D Matrix

## Description

This project involves implementing an in-place algorithm to rotate an \( n \times n \) 2D matrix by 90 degrees clockwise. The primary goal is to manipulate the matrix in-place without using extra space, thus optimizing the space complexity.

### Key Concepts:

1. **Matrix Representation in Python:**
   - Understanding how 2D matrices are represented using lists of lists in Python.
   - Accessing and modifying elements in a 2D matrix.

2. **In-place Operations:**
   - Performing operations on data without creating a copy of the data structure.
   - Minimizing space complexity by modifying the matrix in place.

3. **Matrix Transposition:**
   - Transposing a matrix by swapping rows and columns.
   - Implementing matrix transposition as a step in the rotation process.

4. **Reversing Rows in a Matrix:**
   - Manipulating rows of a matrix by reversing their order as part of the rotation process.

5. **Nested Loops:**
   - Using nested loops to iterate through 2D data structures like matrices.
   - Modifying elements within nested loops to achieve the desired rotation.

## Usage

### Function Prototype:

```python
def rotate_2d_matrix(matrix):
    """
    Rotate the matrix 90 degrees clockwise in-place
    """

### Example
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rotate_2d_matrix(matrix)
print(matrix)
# Output should be:
# [
#     [7, 4, 1],
#     [8, 5, 2],
#     [9, 6, 3]
# ]

### Author
-- Nontuthuzelo Ngwenya
-- Github: DeeGemini

### License
-- None
