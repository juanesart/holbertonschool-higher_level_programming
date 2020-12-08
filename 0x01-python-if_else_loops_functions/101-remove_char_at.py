#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0:
        return (str)
    str_cpy = ""
    str_cpy = str[:n]
    str_cpy += str[n + 1:]
    return (str_cpy)
