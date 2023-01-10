#!/usr/bin/python3

def write_file(filename="", text=""):
    """writes a string to utf-8 text file
    """
    with open("filename", 'w', encoding="utf-8") as myFile:
        return myFile.wtite(text)
