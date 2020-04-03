import os
import fcntl
import subprocess

def list_drives():
    with open("/proc/sys/dev/cdrom/info", "r") as cdinfo:
        all_lines = cdinfo.readlines()
    result = all_lines[2].split()
    result.pop(0)
    result.pop(0)
    return result

def get_volname(drive):
    volname = subprocess.run(["blkid -s LABEL -o value", "/dev/" + drive], stdout=subprocess.PIPE, shell=True).stdout.decode("utf-8")
    return ''.join(volname.split())

def get_status(drive):
    # From https://superuser.com/a/1367091/1014753
    # codes:
    # 1 - no disc
    # 2 - tray is open
    # 3 - determining
    # 4 - disc is in tray
    device = os.open("/dev/" + drive, os.O_RDONLY | os.O_NONBLOCK)
    status = fcntl.ioctl(device, 0x5326)
    os.close(device)
    return status

def get_sector_size(drive):
    sectorsize  = subprocess.run(["blkid -s BLOCK_SIZE -o value", "/dev/" + drive], stdout=subprocess.PIPE, shell=True).stdout.decode("utf-8")
    return ''.join(sectorsize.split())
