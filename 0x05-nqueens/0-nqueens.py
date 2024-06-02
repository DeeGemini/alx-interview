#!/usr/bin/python3
import sys

def is_safe(board, row, col, N):
    """
    Check if the queen at (row, col) is safe from other queens
    Args:
        board (list): List representation of the NxN chessboard
        row (int): Row position of the queen to be placed
        col (int): Column position of the queen to be placed
        N (int): Size of the chessboard
    Returns:
        bool: True if the queen is safe, False otherwise
    """
    # Check if the indices are within the boundaries
    if row >= N or col >= N:
        return False
    
    # Check if the queen is in the same row, diagonal or anti-diagonal
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    
    # Queen is safe
    return True

def solve_nqueens(N, row, board, solutions):
    if row == N:
        solutions.append(board[:])
        return

    # Check if the board is initialized
    if not board:
        board = [-1] * N
    
    for col in range(N):
        # Check if the position is safe
        if is_safe(board, row, col, N):
            # Add the queen to the board
            board[row] = col
            # Recursively solve the next row
            solve_nqueens(N, row + 1, board, solutions)

def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * N
    solutions = []
    solve_nqueens(N, 0, board, solutions)

    for solution in solutions:
        # Check if the solution is valid
        if len(solution) != N:
            print("Invalid solution")
            break

        print([[i, solution[i]] for i in range(N)])

if __name__ == "__main__":
    main()

