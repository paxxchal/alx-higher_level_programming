#!/usr/bin/python3
# This is a function that prints a string in uppercase followed by a new line.
def uppercase(str):
    """This function takes a string as an argument and prints it in uppercase."""
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:  # check if the character is lowercase
            c = chr(
                ord(c) - 32
            )  # convert it to uppercase by subtracting 32 from its ASCII code
        print("{}".format(c), end="")  # outputs the character without a new line
    print()  # outputs a new line at the end
