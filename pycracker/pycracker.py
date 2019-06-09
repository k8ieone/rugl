#!/usr/bin/python
# Usage: pycracker.py MAXPASSWORDLENGTH HASH CHARACTERS HASHTYPE

# Import required modules

import hashlib
import sys
import itertools
import string
import time

def figure_out_charset(characters):
    
    # Still used, sligthly modified
    # This determines what character set should be used
    # TODO: Calculate the number of possible combinations
    # TODO: Implement more character sets (like !?@ etc)

    if "a" in characters and "A" not in characters and "1" not in characters:
        charset = string.ascii_lowercase
        # possiblecombinations = 
    
    elif "a" in characters and "A" in characters and "1" not in characters:
        charset = string.ascii_letters
    
    elif "a" in characters and "A" in characters and "1" in characters:
        charset = string.ascii_letters + string.digits
    
    elif "a" not in characters and "A" in characters and "1" in characters:
        charset = string.ascii_uppercase + string.digits
    
    elif "a" not in characters and "A" not in characters and "1" in characters:
        charset = string.digits
    
    elif "a" in characters and "A" not in characters and "1" in characters:
        charset = string.ascii_lowercase + string.digits
    
    elif "a" not in characters and "A" in characters and "1" not in characters:
        charset = string.ascii_uppercase
    print("The characters the password could contain are these:", charset)
    return charset

# From https://stackoverflow.com/a/48389007
# First one that seems to work as intended
# Returns the password in plaintext
def solve_md5(hash, maxlen, charset):
    print("Starting to crack a MD5 hash...")
    print("...in 5")
    time.sleep(1)
    print("......4")
    time.sleep(1)
    print("......3")
    time.sleep(1)
    print("......2")
    time.sleep(1)
    print("......1")
    time.sleep(1)
    print("......0")
    print("Now cracking!")
    print("Please be patient!")
    # hash_cracked = False
    # attemptno = 0

    # Calculating stuff
    for i in range(maxlen+1):
        for attempt in itertools.product(charset, repeat=i):
            # print(''.join(attempt)) # Uncomment in order to print the current candidate
            # attemptno += 1
            if hashlib.md5(''.join(attempt).encode('utf-8')).hexdigest() == hash:
                # hash_cracked = True
                print("Hash cracked!")
                print(hashlib.md5(''.join(attempt).encode('utf-8')).hexdigest(), "-", ''.join(attempt))
                return ''.join(attempt)
            # elif hash_cracked is False and len(''.join(attempt)) == maxlen:
                # print("Hash not found :(")
                # print(hash, "- ???")

solve_md5(sys.argv[-3], int(sys.argv[-4]), figure_out_charset(sys.argv[-2]))
