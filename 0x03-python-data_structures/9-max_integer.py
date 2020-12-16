#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        biggest = my_list[0]
        for a in range(1, len(my_list)):
            if my_list[a] > biggest:
                biggest = my_list[a]
        return biggest
    else:
        return None
