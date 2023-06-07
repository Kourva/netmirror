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
from urllib.parse import urlparse


#*# Mirrors
mirrors = [
    "https://mirrors.dotsrc.org/artix-linux",
    "https://mirror.clarkson.edu/artix-linux",
    "http://ftp.ntua.gr/pub/linux/artix-linux",
    "https://ftp.sh.cvut.cz/artix-linux",
    "https://mirrors.dotsrc.org/artix-linux",
    "https://mirror.one.com/artix",
    "https://artix.cccp.io",
    "https://ftp.crifo.org/artix",
    "https://mirror.opensrv.org/artixlinux",
    "https://quantum-mirror.hu/mirrors/pub/artix-linux",
    "https://mirror.netcologne.de/artix-linux",
    "http://mirrors.redcorelinux.org/artixlinux",
    "https://mirror.pascalpuffke.de/artix-linux",
    "https://ftp.uni-bayreuth.de/linux/artix-linux",
    "https://ftp.halifax.rwth-aachen.de/artixlinux",
    "https://artix.unixpeople.org",
    "https://mirror1.artixlinux.org",
    "https://eu-mirror.artixlinux.org",
    "https://ftp.cc.uoc.gr/mirrors/linux/artixlinux",
    "http://ftp.ntua.gr/pub/linux/artix-linux",
    "https://mirrors.qontinuum.space/artixlinux",
    "https://artix.sakamoto.pl",
    "https://ftp.ludd.ltu.se/mirrors/artix",
    "https://mirror.linux.pizza/artix-linux",
    "https://artix.kurdy.org",
    "http://artist.artixlinux.org",
    "https://mirror.vinehost.net/artix-linux",
    "https://artix.wheaton.edu",
    "https://mirror.clarkson.edu/artix-linux",
    "https://mirrors.rit.edu/artixlinux",
    "https://mirrors.ocf.berkeley.edu/artix-linux",
    "http://www.nylxs.com/mirror",
    "https://mirrors.nettek.us/artix-linux",
    "https://us-mirror.artixlinux.org",
    "https://mirror.csclub.uwaterloo.ca/artixlinux",
    "https://gnlug.org/pub/artix-linux",
    "https://mirror1.cl.netactuate.com/artix",
    "https://mirrors.tuna.tsinghua.edu.cn/artixlinux",
    "https://mirrors.aliyun.com/artixlinux",
    "https://mirror.nju.edu.cn/artixlinux",
    "https://mirror.albony.xyz/artix",
    "https://mirror.funami.tech/artix",
    "https://mirror.freedif.org/Artix",
    "https://mirrors.cloud.tencent.com/artixlinux",
    "https://mirrors.42tm.tech/artix-linux",
    "https://mirror.aarnet.edu.au/pub/artix"
]

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
        ipadrs = ipaddr(mirror)
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
