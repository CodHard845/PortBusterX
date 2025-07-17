"""
🚀 PortBuster

PortBuster is a lightweight Python-based TCP port scanner that lets you scan open, closed, or filtered ports on a target host — with style 🧑‍💻

No need for heavy tools like Nmap — this one's simple, fast, and speaks emoji 😎

✨ Features:
- 🔧 Scan well-known ports (1–1024)
- 🎯 Custom port selection (e.g., 22, 80, 443)
- 💣 Full-range scan (1–65535) — for the brave ones
- ⏱️ Adjustable timeout (great for slower networks)
- 📟 Clean and readable output

💻 Example usage:
> python portbuster.py

You'll be prompted like this:

    Enter target IP address: 192.168.1.1
    🔧 Scan mode:
      [1] Ports 1 to 1024
      [2] Custom ports (e.g., 22,80,443)
      [3] Full scan (1 to 65535) 🧨💣💥
    Select scan mode (1/2/3): 2
    ⏱️  Enter timeout in seconds (default = 2): 1

⚠️ Disclaimer:
This tool is for educational and authorized use only.  
Do NOT use it to scan targets you don’t own or have no permission to test.  
Or the FBI van might come knocking 🚐🕵️‍♂️

👨‍💻 Author:
Created by @CodHard845  
License: MIT
"""

import socket
import os

def scan_ports(target, ports, timeout=2):
    print(f"\nScanning {target} on {len(ports)} ports (timeout={timeout}s)\n")
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((target, port))

        if result == 0:
            print(f"[+] Port {port} is OPEN")
        else:
            try:
                error_msg = os.strerror(result)
            except ValueError:
                error_msg = "Unknown error"
            print(f"[-] Port {port} is closed or filtered (Error code {result}: {error_msg})")
        sock.close()

if __name__ == "__main__":
    target_ip = input("Enter target IP address: ")

    print("🔧 Scan mode:")
    print("  [1] Ports 1 to 1024")
    print("  [2] Custom ports (e.g., 22,80,443)")
    print("  [3] Full scan (1 to 65535) 🧨💣💥")

    mode = input("Select scan mode (1/2/3): ")

    if mode == "1":
        ports_to_scan = list(range(1, 1025))
    elif mode == "2":
        port_input = input("Enter ports to scan (comma separated): ")
        try:
            ports_to_scan = [int(p.strip()) for p in port_input.split(',')]
        except ValueError:
            print("⛔ Invalid ports list.")
            exit(1)
    elif mode == "3":
        ports_to_scan = list(range(1, 65536))
    else:
        print("⛔ Invalid mode.")
        exit(1)

    timeout_input = input("⏱️  Enter timeout in seconds (default = 2): ").strip()
    if timeout_input == "":
        timeout_value = 2
    else:
        try:
            timeout_value = float(timeout_input)
        except ValueError:
            print("⛔ Timeout must be a number like 1.5 or 3")
            exit(1)

    scan_ports(target_ip, ports_to_scan, timeout=timeout_value)

"""
📜 MIT License

Copyright (c) 2025 CodHard845

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the “Software”), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""
