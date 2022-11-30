#!/usr/bin/python3
def uppercase(str):
    for i in str:
        unicodeNum = ord(i)
        if unicodeNum == 32:
            continue
        unicodeNum -= 32
        char = chr(unicodeNum)
        print(f'{char}', end='')
    print()
