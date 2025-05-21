# AP-TooL (Android Pentest Tool)

**AP-TooL** is a Python-based penetration testing utility designed for Android (Termux) or Linux environments. It provides various modules for basic security auditing and network testing tasks.

## Features

- **Wi-Fi Scanner** – Displays nearby Wi-Fi networks (requires Termux and appropriate permissions).
- **Port Scanner** – Scans common ports (21, 22, 23, 25, 53, 80, 443, 8080) on a target IP.
- **Web Vulnerability Tester** – Basic testing for SQL Injection and XSS vulnerabilities.
- **Brute-force Login Tester** – Attempts brute-force attacks on a given login form.
- **Device Info Collector** – Shows system and network configuration info.
- **Session Sniffer** – Captures live traffic on `wlan0` interface (requires root).
- **File Hasher** – Generates MD5 hash for a specified file.

## Installation

1. **Install required packages**:
   ```bash
   apt install git -y
   or pkg install git -y for termux
   pip install requests pyfiglet subprocess socket
2. **Launch tool**
   ```
   git clone https://github.com/midotech1/AP-TOOL.git
   cd AP-TOOL
   python aptool.py
## Disclamer
This tool is intended only for educational and ethical hacking purposes. Do not use it to target systems without proper authorization. The developer assumes no responsibility for any misuse or
