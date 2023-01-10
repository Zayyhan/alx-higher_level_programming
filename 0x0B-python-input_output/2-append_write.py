#!/usr/bin/python3

def append_write(filename="", text=""):
    """appends a string at the end of utf-8 text file
    """
    with open('filename', mode='a', encoding='utf-8') as myFile:
        return myFile.write(text)
