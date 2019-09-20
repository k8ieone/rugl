#!/bin/bash
# The teacher wouldn't let us finish this in class, so I ignored her solution and did it my way.
# Also she kept me from focusing by always talking! So this is not the finished version...
# -------------------------------------------------------------------------------------------------
# Notes for myself: 
# Subtract 26!
# Use ord and chr
# Also try to do it without ord and chr

import string
import random

def choose_offset():
    offset = random.randrange(1,5)
    return offset

def encode(string, offset):
    ;string_numbers = []
    for i in range(len(string)):
        string_numbers.append(ord(string[i]))
        string_numbers[i] = string_numbers[i + offset]
        new_string = new_string + chr(string_numbers[i])
    return new_string + offset

print(encode("test", 2))
