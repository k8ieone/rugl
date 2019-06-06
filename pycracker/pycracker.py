#!/usr/bin/python
# Usage: pycracker.py HASH CHARACTERS HASHTYPE

import hashlib
import sys
import itertools

def gen_list_of_potential_passwords(characters, length):
    #if "a" in sys.argv[-2] and "A" not in sys.argv[-2] and "1" not in sys.argv[-2]:
    if "a" in characters and "A" not in characters and "1" not in characters:
        alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    elif "a" in characters and "A" in characters and "1" not in characters:
        alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    elif "a" in characters and "A" in characters and "1" in characters:
        alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    
    elif "a" not in characters and "A" in characters and "1" in characters:
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    
    elif "a" not in characters and "A" not in characters and "1" in characters:
        alphabet = "0123456789"
    
    elif "a" in characters and "A" not in characters and "1" in characters:
        alphabet = "abcdefghijklmnopqrstuvwxyz0123456789"
    
    elif "a" not in characters and "A" in characters and "1" not in characters:
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    print("Generating possible password candidates...")
    dictionaryofcandidates = {''.join(p) for p in itertools.permutations(alphabet, length)}
    print("Done!")
    return dictionaryofcandidates

# print(gen_list_of_potential_passwords("aA1", 3))
