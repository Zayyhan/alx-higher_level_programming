#!/usr/bin/python3
"""appends a string at the end of utf-8 text file
"""


def append_write(filename="", text=""):
    with open('filename', mode='a', encoding='utf-8') as myFile:
        return myFile.write(text)
