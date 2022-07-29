#!/usr/bin/python3
""" function: text_indentation"""


def text_indentation(text):
    """Args:
        text: string which is going to be broken down with the end flags <. ? :>
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for i in range(len(text)):
        if text[i] in ".?:":
            print(text[i])
            print("")
        else:
            if text[i - 1] in ".?:" and text[i] == " ":
                continue
            else:
                print(text[i], end="")