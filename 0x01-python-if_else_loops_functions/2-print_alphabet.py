#!/usr/bin/env python
# 2-print_alphabet.py

"""Print the alphabet in lowercase, not followed by a new line."""
for letter in range(97, 123):
    print("{}".format(chr(letter)), end="")
