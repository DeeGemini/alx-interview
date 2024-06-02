# N Queens Problem Solver

## Description
The N Queens puzzle is a classic problem in computer science and combinatorial mathematics. The challenge is to place N non-attacking queens on an N×N chessboard. This program provides a solution to the N Queens problem using a backtracking algorithm.

## Requirements
- **Python Version**: This project is developed and tested with Python 3.4.3.
- **Operating System**: The code is intended to run on Ubuntu 20.04 LTS.
- **Editors**: The code should be edited using `vi`, `vim`, or `emacs`.

## Usage
To run the program, use the following command:
- ./0-nqueens.py N
- `N`: The size of the chessboard (must be an integer greater than or equal to 4).

### Example
```bash
./0-nqueens.py 4
- This will output all possible solutions for the 4 Queens problem.

## Error Handling
- The program handles the following error scenarios:

- If the number of arguments is incorrect, it prints:
Usage: nqueens N
- If N is not an integer, it prints:
N must be a number
- If N is less than 4, it prints:
N must be at least 4

## Implementation Details
- The solution is implemented using a backtracking algorithm. The main idea is to place queens one by one in different columns, starting from the leftmost column. When placing a queen, it checks for clashes with already placed queens. If a clash is found, it backtracks and tries the next position.

## Files
- nqueens.py: The main script to solve the N Queens problem.
- README.md: This file, containing the description and instructions for the project.

## Author
DeeGemini

## License
This project is provided without any license.
