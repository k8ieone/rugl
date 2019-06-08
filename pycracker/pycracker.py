#!/usr/bin/python
# Usage: pycracker.py PASSWORDLENGTH HASH CHARACTERS HASHTYPE

# Import required modules

import hashlib
import sys
# import itertools

def figure_out_charset(characters):
    
    # Still used, sligthly modified
    # This determines what character set should be used
    # TODO: Calculate the possible combinations

    if "a" in characters and "A" not in characters and "1" not in characters:
        charset = "abcdefghijklmnopqrstuvwxyz"
        #possiblecombinations = 
    
    elif "a" in characters and "A" in characters and "1" not in characters:
        charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    elif "a" in characters and "A" in characters and "1" in characters:
        charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    
    elif "a" not in characters and "A" in characters and "1" in characters:
        charset = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    
    elif "a" not in characters and "A" not in characters and "1" in characters:
        charset = "0123456789"
    
    elif "a" in characters and "A" not in characters and "1" in characters:
        charset = "abcdefghijklmnopqrstuvwxyz0123456789"
    
    elif "a" not in characters and "A" in characters and "1" not in characters:
        charset = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    #print("Generating possible password candidates...")
    #listofcandidates = [''.join(p) for p in itertools.combinations_with_replacement(alphabet, length)]
    #currentcandidate = ''.join(p) for p in itertools.combinations_with_replacement(alphabet, length)
    #print("Done!")
    return charset

def allperm(inputstr):
    # From: http://code.activestate.com/recipes/577842-get-all-possible-combinations-of-characters-given-/
    for i in range(len(inputstr)):
        yield(inputstr[i])        
        for s in allperm(inputstr[:i] + inputstr[i+1:]):
            yield(inputstr[i] + s)

"""
def determine_hash(candidate_list):
    # Currently unused
    # Pretty useless when only having one possible hashtype
    
    if sys.argv[-1] == "MD5":
        calculate_md5(candidate_list)
"""
# Pretty useless even with multiple hashes

"""
def calculate_md5(candidate_list):
    # Currently usnused
    # The old way of doing things
    # Finally! Calculate the MD5 hash for each of the candidates and compare it to the original

    hash_cracked = False
    print("Searching for a match...")

    for i in range(len(candidate_list)):
        #currentcandidate = ''.join(i) allperm("abcde")
        if hashlib.md5(candidate_list[i].encode('utf-8')).hexdigest() == str(sys.argv[-3]):
            hash_cracked = True
            print("Hash cracked!")
            print(hashlib.md5(candidate_list[i].encode('utf-8')).hexdigest())
            print(candidate_list[i])
            return candidate_list[i]
        
        elif possiblecombinations == i and hash_cracked is False:
            print("Hash not found :(")
"""
# I dunno... Maybe I should give up?
# I feel like I am getting closer and further away at the same time

#determine_hash(gen_list_of_potential_passwords(sys.argv[-2], int(sys.argv[-4])))

def get_candidate_and_calculate(hashtype, characterset):
    for currentcandidate in allperm(characterset):
        print(hashlib.md5(currentcandidate.encode('utf-8')).hexdigest(),currentcandidate)
        if hashtype == "MD5":
            if hashlib.md5(currentcandidate.encode('utf-8')).hexdigest() == sys.argv[-3]:
                # hash_cracked = True
                # Usunsed variable
                # TODO: Make it used (create elif operation failed or sth like that)
                print("Hash cracked!")
                print(hashlib.md5(currentcandidate.encode('utf-8')).hexdigest())
                print(currentcandidate)
                return currentcandidate

get_candidate_and_calculate(sys.argv[-1], figure_out_charset(sys.argv[-2]))