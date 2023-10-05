#!/usr/bin/python3
import sys
import hidden_4
if __name__ == "__main__":
    assert sys.version_info >= (3, 8)
    content = dir(hidden_4)
    filtered_content = [name for name in content if not name.startswith("__")]
    sorted_content = sorted(filtered_content)
    for name in sorted_content:
        print(f"{name}")
