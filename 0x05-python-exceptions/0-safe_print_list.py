#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        while count < x:
            for i in my_list:
                print(i)
                count += 1
        return count
    except:
        print("Oops! Something went wrong")
