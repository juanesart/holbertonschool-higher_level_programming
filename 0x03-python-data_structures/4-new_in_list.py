#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list:
        listcpy = []
        listcpy[:] = my_list[:]
        if idx < 0:
            return listcpy
        if idx >= len(my_list):
            return listcpy
        else:
            listcpy[idx] = element
            return listcpy
