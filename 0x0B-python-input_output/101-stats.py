#!/usr/bin/python3
"""Defines a module 101-stats."""


import sys
"""Imports a module sys."""


def print_metrics(total_size, status_codes):
    """Defines a function called print_metrics, prints metrics."""

    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


if __name__ == "__main__":
    count = 0
    total_size = 0
    status_codes = {"200": 0, "301": 0, "400": 0, "401": 0,
                    "403": 0, "404": 0, "405": 0, "500": 0}

    try:
        for line in sys.stdin:
            count += 1
            split_line = line.split()
            try:
                size = int(split_line[-1])
                total_size += size
            except:
                pass
            try:
                code = split_line[-2]
                if code in status_codes:
                    status_codes[code] += 1
            except:
                pass
            if count % 10 == 0:
                print_metrics(total_size, status_codes)

    except KeyboardInterrupt:
        print_metrics(total_size, status_codes)
        raise
