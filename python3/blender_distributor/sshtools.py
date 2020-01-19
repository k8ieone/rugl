#!/usr/bin/env python

import os

def read_file(filename):
    with open(filename, "r") as file1:
        ip_list = file1.readline().split()
    return ip_list

def setup_node(ipaddr, mountpoint):
    command = "ssh " + ipaddr + " sudo mount " + mountpoint
    os.system(command)

def start_node(ipaddr, blendfile, blenderpath, framename):
    command = "ssh " + ipaddr + " screen -d -m " + blenderpath + " -b " + blendfile + " -o " + framename + " -a"
    print(command)
    os.system(command)
