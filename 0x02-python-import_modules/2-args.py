#!/usr/bin/python3
import sys
if __name__ == "__main__":
    argv = sys.argv
    if len(argv) < 2:
        print(f"{0:d} arguments.")
    elif len(argv) == 2:
        print(f"{1:d} argument:")
        print(f"{1:d}: {sys.argv[1]}")
    else:
        print(f"{(len(argv) - 1):d} arguments:")
        for i, args in enumerate(sys.argv[1:], start=1):
            print(f"{i:d}: {args}")
