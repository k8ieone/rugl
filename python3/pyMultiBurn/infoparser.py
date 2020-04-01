def list_drives():
    with open("/proc/sys/dev/cdrom/info", "r") as cdinfo:
        all_lines = cdinfo.readlines()
    result = all_lines[2].split()
    result.pop(0)
    result.pop(0)
    return result
