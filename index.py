# Detect the technology used by a website
import builtwith
from colorama import Fore, init
import socket
from ipwhois import IPWhois
from pprint import pprint
import time

# init colorama
init()

site = input("Enter Domain: ")

# beautiful desing
progress = "="
counter = 0
for i in range(4):
    counter += 25
    progress += "==="
    time.sleep(1)
    print(progress+str(counter)+"%")
# --------------

# ip whois
# information about server
ip = socket.gethostbyname(site)
server = IPWhois(ip)
server = server.lookup_whois()
# ---------------

# builtwith
res = builtwith.builtwith("https://"+site)


print("Site Technology: \n")
for i in res:
    print(Fore.GREEN+i, res[i])


print(Fore.WHITE,"-------------------")
print("Server Information: \n")


print(Fore.RED)
pprint(server)
