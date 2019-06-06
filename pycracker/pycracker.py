#!/usr/bin/python
# Usage: pycracker.py PASSWORDLENGTH HASH CHARACTERS HASHTYPE

# Import required modules

import hashlib
import sys
import itertools

def gen_list_of_potential_passwords(characters, length):
    
    # This determines what character set should be used

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
    listofcandidates = [''.join(p) for p in itertools.permutations(alphabet, length)]
    print("Done!")
    return listofcandidates

def determine_hash(candidate_list):
    
    # Pretty useless when only having one possible hashtype
    
    if sys.argv[-1] == "MD5":
        calculate_md5(candidate_list)

def calculate_md5(candidate_list):

    # Finally! Calculate the MD5 hash for each of the candidates and compare it to the original

    hash_cracked = False
    print("Searching for a match...")

    for i in range(len(candidate_list)):
        if hashlib.md5(candidate_list[i].encode('utf-8')).hexdigest() == str(sys.argv[-3]):
            hash_cracked = True
            print("Hash cracked!")
            print(hashlib.md5(candidate_list[i].encode('utf-8')).hexdigest())
            print(candidate_list[i])
            return candidate_list[i]
        
        elif len(candidate_list) == i + 1 and hash_cracked is False:
            print("Hash not found :(")

determine_hash(gen_list_of_potential_passwords(sys.argv[-2], int(sys.argv[-4])))
