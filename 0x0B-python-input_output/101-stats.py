#!/usr/bin/python3
import sys

file_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
count = 0

try:
    for line in sys.stdin:
        count += 1
        line = line.split()
        try:
            file_size += int(line[-1])
        except (IndexError, ValueError):
            pass
        try:
            status_codes[int(line[-2])] += 1
        except (IndexError, ValueError):
            pass

        if count % 10 == 0:
            print("File size: {}".format(file_size))
            for code in sorted(status_codes.keys()):
                if status_codes[code] > 0:
                    print("{}: {}".format(code, status_codes[code]))

except KeyboardInterrupt:
    print("File size: {}".format(file_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))
