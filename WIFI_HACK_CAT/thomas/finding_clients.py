from scapy.all import *
macs = []
def hopper(iface):
    n = 1
    stop_hopper = False
    while not stop_hopper:
        time.sleep(0.50)
        os.system('iwconfig %s channel %d' % (iface, n))
        dig = int(random.random() * 14)
        if dig != 0 and dig != n:
            n = dig
def analyzer(packet):
    if packet.haslayer(Dot11ProbeResp) and packet[Dot11FCS]:
        new  = packet[Dot11FCS].addr2
        cl =  packet[Dot11FCS].addr1
        if new not in macs:
            macs.append(new)
            print(f"[+]ACCESS POITN :{new}[+] ----> CLIENT : {cl}")
def start(iface):
    thread = threading.Thread(target=hopper, args=(iface,), name="hopper")
    thread.daemon = True
    thread.start()
    sniff(iface=iface,prn=analyzer)