#!/usr/bin/python
# Usage: pycracker.py MAXPASSWORDLENGTH HASH CHARACTERS HASHTYPE NTHREADS

# Import required modules
import hashlib
import sys
import itertools
import string
import threading

def figure_out_charset(characters):
    # Maybe this could be done a bit better?
    # This determines what character set should be used and calculates the number of possible combinations

    if "a" in characters and "A" not in characters and "1" not in characters and "@" not in characters:
        charset = string.ascii_lowercase
    
    elif "a" in characters and "A" in characters and "1" not in characters and "@" not in characters:
        charset = string.ascii_letters
    
    elif "a" in characters and "A" in characters and "1" in characters and "@" not in characters:
        charset = string.ascii_letters + string.digits
    
    elif "a" not in characters and "A" in characters and "1" in characters and "@" not in characters:
        charset = string.ascii_uppercase + string.digits
    
    elif "a" not in characters and "A" not in characters and "1" in characters and "@" not in characters:
        charset = string.digits
    
    elif "a" in characters and "A" not in characters and "1" in characters and "@" not in characters:
        charset = string.ascii_lowercase + string.digits
    
    elif "a" not in characters and "A" in characters and "1" not in characters and "@" not in characters:
        charset = string.ascii_uppercase
    
    elif "a" in characters and "A" in characters and "1" in characters and "@" in characters:
        charset = string.printable
    
    elif "a" in characters and "A" not in characters and "1" not in characters and "@" in characters:
        charset = string.ascii_lowercase + string.punctuation
    
    elif "a" not in characters and "A" in characters and "1" not in characters and "@" in characters:
        charset = string.ascii_uppercase + string.punctuation
    
    elif "a" not in characters and "A" not in characters and "1" in characters and "@" in characters:
        charset = string.digits + string.punctuation
    
    elif "a" in characters and "A" in characters and "1" not in characters and "@" in characters:
        charset = string.ascii_letters + string.punctuation
    
    elif "a" in characters and "A" not in characters and "1" in characters and "@" in characters:
        charset = string.ascii_lowercase + string.digits + string.punctuation
    
    elif "a" not in characters and "A" in characters and "1" in characters and "@" in characters:
        characters = string.ascii_uppercase + string.digits + string.punctuation
    
    charset_and_possiblecombinations = [charset, len(charset) ** int(sys.argv[-5])]
    print("Possible combinations:", charset_and_possiblecombinations[1])
    print("Characterset:", charset_and_possiblecombinations[0])
    return charset_and_possiblecombinations

# From https://stackoverflow.com/a/48389007
# Returns the password in plaintext
def solve_md5_orig(userhash, maxlen, charset, possiblecombinations):
    print("Starting to crack a MD5 hash...")
    print("Please be patient!")
    hash_cracked = False
    attemptno = 0
    # Calculating stuff
    for i in range(maxlen+1):
        for attempt in itertools.product(charset, repeat=i):
            # print(''.join(attempt)) # Uncomment in order to print the current candidate
            attemptno += 1
            if hashlib.md5(''.join(attempt).encode('utf-8')).hexdigest() == userhash:
                hash_cracked = True
                print("\n\nHash cracked!")
                print(hashlib.md5(''.join(attempt).encode('utf-8')).hexdigest(), "-", ''.join(attempt),"\n")
                return ''.join(attempt)
            elif hash_cracked is False and attemptno == possiblecombinations:
                print("\n\nI tried", possiblecombinations, "different passwords and none of them worked")
                print("Hash not found :(")
                print(userhash, "- ???\n")
                return None

def solve_md5_mt():
    pass

# charset_and_possiblecombinations = figure_out_charset(sys.argv[-3])
# solve_md5(sys.argv[-4], int(sys.argv[-5]), charset_and_possiblecombinations[0], int(charset_and_possiblecombinations[1]))

def control_thread():
    # Get the number of cores and divide the possible combinations by the number of threads
    # Make a function, that would try the different passwords in the specified range
    # I will probably make a dictionary of all the password candidates and their hashes for each thread
    # Then they will be merged and searched for the specified hash
    possiblecombinations = figure_out_charset(sys.argv[-3])[1]
    combs_per_thread = int(possiblecombinations / sys.argv[-1])
    pass
