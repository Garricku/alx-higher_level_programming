#!/usr/bin/python3
import sys

def nqueens(N, board=[], row=0):
    if row == N:
        print(str([[r, c] for r, c in enumerate(board)]))
        return

    for col in range(N):
        if all(col != c and row - r != abs(col - c) for r, c in enumerate(board)):
            nqueens(N, board + [col], row + 1)

if __name__ == "__main__":
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

    nqueens(N)
