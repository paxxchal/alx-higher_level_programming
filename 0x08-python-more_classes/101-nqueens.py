#!/usr/bin/python3
"""This module defines a program that solves the N queens problem"""

import sys


def is_safe(board, row, col, n):
    """Checks if a queen can be placed in a given spot"""
    # Check the same column
    for i in range(row):
        if board[i][col] == 1:
            return False
    # Check the upper left diagonal
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1
    # Check the upper right diagonal
    i = row
    j = col
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1
    # The spot is safe
    return True


def solve_nqueens(board, row, n, solutions):
    """Solves the N queens problem using backtracking"""
    # Base case: all queens are placed
    if row == n:
        # Print the solution
        solution = []
        for i in range(n):
            for j in range(n):
                if board[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return
    # Try all spots in the current row
    for col in range(n):
        # Check if the spot is safe
        if is_safe(board, row, col, n):
            # Place a queen
            board[row][col] = 1
            # Recur for the next row
            solve_nqueens(board, row + 1, n, solutions)
            # Remove the queen (backtrack)
            board[row][col] = 0


if __name__ == "__main__":
    # Check the number of arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    # Check if the argument is a number
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    # Check if the number is at least 4
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    # Create an empty board
    board = [[0 for i in range(n)] for j in range(n)]
    # Create an empty list of solutions
    solutions = []
    # Solve the problem
    solve_nqueens(board, 0, n, solutions)
    # Print the solutions
    for solution in solutions:
        print(solution)
