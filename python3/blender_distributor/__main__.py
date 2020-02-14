#!/usr/bin/env python

import sys
import sshtools

if "start" in sys.argv[1]:
    blender_path = sys.argv[-4]
    ipaddr_file = sys.argv[-3]
    blend_file = sys.argv[-2]
    frame_name = sys.argv[-1]
    opmode = "start"
elif "setup" in sys.argv[1]:
    ipaddr_file = sys.argv[-2]
    mount_point = sys.argv[-1]
    opmode = "setup"
else:
    print("Operation " + sys.argv[1] + " is not valid!")
    print("Usage: ")
    print("python __main__.py setup IP_FILE MOUNT_POINT")
    print("python __main__.py start BLENDER_EXECUTABLE IP_FILE BLEND_FILE OUTPUP_PATH\n")
    print("https://github.com/satcom886/rugl/tree/master/python3/blender_distributor")
    sys.exit(1)

if opmode == "setup":
    ip_list = sshtools.read_file(ipaddr_file)
    for ip in ip_list:
        sshtools.setup_node(ip, mount_point)
elif opmode == "start":
    ip_list = sshtools.read_file(ipaddr_file)
    for ip in ip_list:
        sshtools.start_node(ip, blend_file, blender_path, frame_name)