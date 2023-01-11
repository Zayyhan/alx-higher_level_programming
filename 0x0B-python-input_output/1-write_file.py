#!/usr/bin/python3
"""writes a string to utf-8 text file
"""


def write_file(filename="", text=""):
  with open("filename", 'w', encoding="utf-8") as myFile:
        return myFile.wtite(text)
