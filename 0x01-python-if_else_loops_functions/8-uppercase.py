#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord('a') <= ord(i) <= ord('z'):
            i = chr(ord(i) - 32)
        print(f'{i}', end='')
    print()
