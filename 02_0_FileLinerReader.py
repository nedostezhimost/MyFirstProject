#!/usr/bin/env python3
import sys
if len(sys.argv) < 2:
    print("Error: Please provide a filename.")
    print("Usage: ./02_0FileLinerReader.py <filename>")
    sys.exit(1)
filename = sys.argv[1]
try:
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            # end=''
            print(line, end='')
except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
