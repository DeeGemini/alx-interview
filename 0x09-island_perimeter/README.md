# Island Perimeter Project

## Description

The Island Perimeter project is designed to apply knowledge of algorithms, data structures (specifically matrices or 2D lists), and iterative or conditional logic to solve a geometric problem within a grid context. The goal is to calculate the perimeter of a single island in a grid, where the grid is represented by a 2D array of integers.

## Concepts

- **2D Arrays (Matrices)**: Accessing and iterating over elements in a 2D array, understanding how to navigate through adjacent cells (horizontally and vertically).
- **Conditional Logic**: Applying conditions to determine whether a cell contributes to the perimeter of the island.
- **Counting Techniques**: Developing a method to count the edges that contribute to the island’s perimeter.
- **Problem-Solving Strategies**: Breaking down the problem into smaller tasks, such as identifying land cells and calculating their contribution to the perimeter.
- **Python Programming**: Using nested loops for iterating over grid cells and conditional statements to check the status of adjacent cells.

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.4.3)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- Code should use the PEP 8 style (version 1.7)
- No imports of external modules
- All modules and functions must be documented
- All files must be executable

## Task

### 0. Island Perimeter

Create a function `def island_perimeter(grid):` that returns the perimeter of the island described in `grid`:

- `grid` is a list of list of integers:
  - `0` represents water
  - `1` represents land
- Each cell is square, with a side length of 1
- Cells are connected horizontally/vertically (not diagonally)
- The grid is rectangular, with its width and height not exceeding 100
- The grid is completely surrounded by water
- There is only one island (or nothing)
- The island doesn’t have “lakes” (water inside that isn’t connected to the water surrounding the island)

## Usage

Here is the implementation of the `island_perimeter` function:

```python
#!/usr/bin/python3

def island_perimeter(grid):
    """
    Calculate the perimeter of the island in the given grid.
    
    Args:
    grid (list of list of int): 2D list representing the grid (0: water, 1: land).
    
    Returns:
    int: The perimeter of the island.
    """
    perimeter = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1:
                # Check if the cell to the top is water or out of bounds
                if row == 0 or grid[row - 1][col] == 0:
                    perimeter += 1
                # Check if the cell to the bottom is water or out of bounds
                if row == len(grid) - 1 or grid[row + 1][col] == 0:
                    perimeter += 1
                # Check if the cell to the left is water or out of bounds
                if col == 0 or grid[row][col - 1] == 0:
                    perimeter += 1
                # Check if the cell to the right is water or out of bounds
                if col == len(grid[0]) - 1 or grid[row][col + 1] == 0:
                    perimeter += 1
    return perimeter

** Example
- Given the following grid:
[
  [0, 1, 0, 0],
  [1, 1, 1, 0],
  [0, 1, 0, 0],
  [1, 1, 0, 0]
]
Calling 'island_perimeter(grid)' would return '16'.

** Testing
- To test the function, you can create a script or use a Python interactive shell:
grid = [
    [0, 1, 0, 0],
    [1, 1, 1, 0],
    [0, 1, 0, 0],
    [1, 1, 0, 0]
]

print(island_perimeter(grid))  # Output should be 16

** License
- None

** Author
- Nontuthuzelo Ngwenya
- Github : DeeGemini
