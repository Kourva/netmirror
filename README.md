<h3 align='left'>
    <img align="left" src="https://github.com/kozyol/netmirror/assets/118578799/872f1e85-dafd-4328-9f5a-69161cceec81" width=120  height=120>
    <h1>netmirror</h1>
  <p><b>ArtixLinux Mirror Optimizer. Selects fastest mirror in mirrors based on ping ms</b></p>
</h3>

<br><br>

# ▍Preview
Mirror list is inside the main script. so if you want to **add** or **remove** mirrors, edit netmirror file.<br>
Netmirror will ping all mirrors and print the fastest mirror.<br>
Mirrors are for Artix Linux
```bash
$ netmirror
Ping process started on mirrors...
 * mirrors.dotsrc.org                      [130.225.254.116] 159.792 ms █▓▒░
 * mirror.clarkson.edu                     [128.153.145.19 ] 226.728 ms █▓▒░
 * mirror.freedif.org                      [132.147.122.105] 290.100 ms █▓▒░
 * mirror.albony.xyz                       [188.114.99.0   ] 121.820 ms █▓▒░
 * mirrors.cloud.tencent.com               [43.152.29.12   ] 126.056 ms █▓▒░
 * mirrors.42tm.tech                       [103.224.182.249] 286.557 ms █▓▒░
 * mirror.aarnet.edu.au                    [202.158.214.106] 477.169 ms █▓▒░

Fastest mirror: https://mirror.albony.xyz/artix
 * speed: 121.82 ms
```
<br>

# ▍Setup
Installing **netmirror** is so simple. just follow following steps...<br>
▢ **⒈Clone repository**
```bash
git clone https://github.com/kozyol/netmirror
```
▢ **⒉Navigate to netmirror directory**
```bash
cd netmirror/
```
▢ **⒊Make files executable**
```bash
chmod +x install.py netmirror.py
```
▢ **⒋Install the netmirror**
```bash
python install.py
```
<br>

# ▍Uninstall
use installer with --uninstall argument to uninstall the netmirror as follows...
```bash
python install.py --uninstall
```
