#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    while x > 0:
        try:
            print(my_list[i], end='')
            i += 1
            x -= 1
        # If x > number of elemnts in list
        except IndexError:
            break
    # Print newline
    print()
    # Returns the real number of elements printed
    return i
