#!/usr/bin/python3
"""N Queen"""
import sys


def check_queen(board, row, col):
    """Checks if queen can be placed"""
    for r in range(row):
        c = board[r]
        if c == col:
            return False
        if abs(c - col) == abs(r - row):
            return False

    return True


def solutions(board, row, n):
    """Find solutions"""
    if row == n:
        result = [[r, board[r]] for r in range(n)]
        print(result)
        return

    for col in range(n):
        if check_queen(board, row, col):
            board[row] = col
            solutions(board, row + 1, n)


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * n
    solutions(board, 0, n)
