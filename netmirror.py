#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ArtixLinux Mirror Optimizer || netmirror
# Author  : Kourva
# Source  : https://github.com/Kourva/netmirror


#*# Imports
import os
import re
import socket
import subprocess
import requests
from urllib.parse import urlparse



#*# Mirrors
url = "https://gitea.artixlinux.org/packages/artix-mirrorlist/raw/branch/master/mirrorlist"
response = requests.get(url)
response.raise_for_status()

lines = response.text.splitlines()

#*# Remove Comments and irrelevant things
regexs = [
        (r"#.*", ""), # COMMENTS
        (r"Server\ =\ ", ""), # Irrelevant placeholder before server link
]

#*# Get each mirror from lines extracted from mirrorlist raw file, using re to filter out the links
mirrors = []
for i,line in enumerate(lines, start=1):
    for pat, repl in regexs:
        line = re.sub(pat, repl, line)
    if line.strip() == '':
        pass
    else:
        mirrors.append(line.strip())

#*# Ping all mirrors
def ping_mirrors():
    #*# Get Ip address
    ipaddr = lambda url: socket.gethostbyname(urlparse(url).hostname) if urlparse(url).hostname else None

    # Check mirrors
    speeds = {}
    print("Ping process started on mirrors...")

    # Get terminal size
    cols = os.get_terminal_size().columns
    info_bar = cols // 2

    for mirror in mirrors:
        # Get mirror Ip address
        # If server not accessible, then jump it and go to next one.
        try:
            ipadrs = ipaddr(mirror)
        except Exception as e:
            print(f"NOT ACCESSIBLE! : {e}")
            continue

        _, _, name, *_ = mirror.rsplit("/")
        info = name.ljust(info_bar)
        print(f" \33[2;36m*\33[m {info} [\33[2;36m{ipadrs.ljust(15)}\33[m]", end=" ")
        try:
            # Ping mirror
            ping_output = subprocess.check_output(
                ['ping', '-c', '3', '-q', '-i', '0.2', '-w', '1', ipadrs],
                stderr=subprocess.STDOUT,
                universal_newlines=True
            )
            # Find ping ms
            match = re.search(r"= (\d+\.\d+)/", ping_output)
            if match:
                speed_ms = float(match.groups()[0])
                speeds[mirror] = speed_ms
            if speed_ms <= 150:
                print(f"\33[2;32m{match.groups()[0]} ms █▓▒░\33[m", end="\n")
            if speed_ms > 150:
                print(f"\33[2;33m{match.groups()[0]} ms █▓▒░\33[m", end="\n")

        # Cancel progress when user pressed Ctrl+C
        except KeyboardInterrupt:raise SystemExit("\n\33[2;31mGot keyboard Interrupt. Leaving progress!\33[m")
        # Except ping error and set mirror unavailable  
        except:print(f"\33[2;31mFailed     █▓▒░\33[m", end="\n")

    # Return mirrors with ping ms
    return speeds

#*# Update Mirrors
def update_mirrors():
    # Get mirrors speed
    speeds = ping_mirrors()

    # Print no mirrors available if all mirrors down
    if not speeds:print("No mirrors available.")

    # Find the fastest mirror and show save prompt
    else:
        # Sort the mirrors and find best mirror
        best_mirror = min(speeds, key=speeds.get)

        # Print fastest mirror
        print(f"\nFastest mirror:\33[2;36m {best_mirror}\33[m\n \33[2;36m*\33[m speed: {speeds[best_mirror]} ms")

#*# Main section
if __name__ == '__main__':update_mirrors()
else:print("error: you cannot perform this operation unless you are root.")
