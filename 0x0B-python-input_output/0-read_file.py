#!/usr/bin/python3


def read_file(filename=""):
    with open('filename', encoding="utf-8") as myFile:
        print(myFile.read(), end='')
        """reads a text file and prints it to stdout
        """
