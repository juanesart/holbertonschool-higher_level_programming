#!/usr/bin/python3
"""
5-test_indentation module.
text_indentation: prints newlines after certain characters.
"""


def text_indentation(text):
    """splits a text into lines along "?", ":", "." followed by 2 new lines"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    cont = 0
    for a in text:
        if cont == 0:
            if a == ' ':
                continue
            else:
                cont = 1
        if cont == 1:
            if a == '?' or a == '.' or a == ':':
                print(a)
                print()
                cont = 0
            else:
                print(a, end="")
