#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
This module defines a script that
reads stdin line by line and computes metrics
"""
import sys

total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
counter = 0

try:
    for line in sys.stdin:
        counter += 1
        _, _, _, status_code, file_size = line.split(" ")
        total_size += int(file_size)
        status_codes[int(status_code)] += 1

        if counter % 10 == 0:
            print("Total file size: ", total_size)
            for key in sorted(status_codes.keys()):
                if status_codes[key] > 0:
                    print(f"{key}: {status_codes[key]}")

except KeyboardInterrupt:
    print("Total file size: ", total_size)
    for key in sorted(status_codes.keys()):
        if status_codes[key] > 0:
            print(f"{key}: {status_codes[key]}")
