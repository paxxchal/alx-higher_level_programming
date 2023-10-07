#!/usr/bin/python3
def print_list_integer(my_list=[]):
    # Loop through the list using a for loop
    for item in my_list:
        # Print each item using str.format()
        print("{:d}".format(item))
