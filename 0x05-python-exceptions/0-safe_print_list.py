#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    count = 0

    try:
        for i in range(x):
            print(my_list[i], end="")
            count += 1

    except IndexError:
        pass  # Ignore index errors if x is greater than the length of the list

    finally:
        print()
        return count
