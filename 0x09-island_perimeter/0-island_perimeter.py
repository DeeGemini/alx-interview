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
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                # Check if the cell to the top is water or out of bounds
                if row == 0 or grid[row - 1][col] == 0:
                    perimeter += 1
                # Check if the cell to the bottom is water or out of bounds
                if row == rows - 1 or grid[row + 1][col] == 0:
                    perimeter += 1
                # Check if the cell to the left is water or out of bounds
                if col == 0 or grid[row][col - 1] == 0:
                    perimeter += 1
                # Check if the cell to the right is water or out of bounds
                if col == cols - 1 or grid[row][col + 1] == 0:
                    perimeter += 1
    return perimeter

