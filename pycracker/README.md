# What can I do with this?
This program will be able to crack MD5 (and potentionally more) hashes.
## Usage:
pycracker.py HASH CHARACTERS HASHTYPE
# Where are we going with this?
This is a project that aims to create the worlds slowest password cracker. Feel free to hate. My memory management is a mess right now so this program is quite good at eating up RAM. My warning: Do not run it with password length lagrer than 4.
# Why is it consuming so much memory?
I have all the password candidates stored in a single dictionary variable. Messy but works.