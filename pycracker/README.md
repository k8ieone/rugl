# What can I do with this?
This program can crack MD5 hashes (more hashes comming).
## Usage:
pycracker.py **PASSWORDLENGTH HASH CHARACTERS HASHTYPE**
## Possible arguments:
### WARNING: ARGUMENTS MUST BE ALL PRESENT AND IN THE EXACT ORDER ABOVE!
PASSWORDLENGTH - a number that determines the length of the password  
HASH - the hash string  
CHARACTERS - character sets:  
 * a means all the letters of the english alphabet (lowercase)
 * A means uppercase
 * 1 means numbers  
HASHTYPE - type of the hash:
 * MD5
# Where are we going with this?
This is a project that aims to create the worlds slowest password cracker. Feel free to hate. My memory management is a mess right now so this program is quite good at eating up RAM. My warning: Do not run it with password length lagrer than 4.
# Why is it consuming so much memory?
I have all the password candidates stored in a single dictionary variable. Messy but works.
