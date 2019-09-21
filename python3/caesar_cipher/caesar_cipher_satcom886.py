#!/usr/bin/python
# The teacher wouldn't let us finish this in class, so I ignored her solution and did it my way.
# Also she kept me from focusing by always talking! So this is not the finished version...
# -------------------------------------------------------------------------------------------------
# Notes for myself: 
# Subtract 26!
# Also try to do it without ord and chr

import string
import random

def encode(string):
    offset = random.randrange(1, 5)
    string_in_numbers = []
    string_encoded = ""
    for i in range(len(string)):
        string_in_numbers.append(ord(string[i]))
        string_encoded += chr(string_in_numbers[i] + offset)
    return [string_encoded, offset]

print(encode("ahoj"))

def decode(string_encoded, offset):
    string_in_numbers = []
    string_decoded = ""
    for i in range(len(string_encoded)):
        string_in_numbers.append(ord(string_encoded[i]))
        string_decoded += chr(string_in_numbers[i] - offset)
    return string_decoded

print(decode("dkrm#}pugl", 3))
