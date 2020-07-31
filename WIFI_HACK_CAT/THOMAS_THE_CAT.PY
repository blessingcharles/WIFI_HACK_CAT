from termcolor import colored
from thomas import arpspoofer , arp_spoof_detector , dns_spoof , port_scanner , net_cut,mon_mode , wifi_detector , deauthenticate_clients ,fake_access_points,finding_clients

print(colored(r'''
    --------- |     | 0000000    /\    /\     0000   000000000000000000000000000000000000000000000000000000
        |     |_____| 0     0   /  \  /  \   0    0  0                       0000000     0000      00000000
        |     |     | 0     0  /    \/    \  000000  0000000                 0          0    0        0
        |     |     | 0000000 /            \ 0    0         0      \ THE /   0          000000        0
        |                    /              \               0        ___     0000000    0    0        0
        | 000000000000000000000000000000000000000000000000000                                         0
        |                                                                                             0
                                                        --- THE H04X
''',"blue" , attrs=["bold" , "underline"])
)

def get_input():
    return int(input("ENTER THE COMMAND YOU WANT TO EXECUTE BY ENTERING THE NUMBER : "))
if __name__ == "__main__":
    print(colored('''
 
                    [+]  1 . ARP_SPOOF\n
                    [+]  2 . ARP_SPOOF_DETECTOR\n                    
                    [+]  3 . DNS SPOOF\n
                    [+]  4 . CUTTING THE INTERNET CONNECTION FOR A CLIENT\n
                    [+]  5 . PORT SCANNER\n
                    
                    |||||||||||| MONITOR MODE REQUIRED FOR THE FOLLOWING |||||||||||||\n
                    
                    [+]  6 . WIFI DETECTOR ()\n
                    [+]  7 . DEAUTHENTICATE CLIENTS ()\n
                    [+]  8 . FINDING ALL CLIENTS CONNECTED TO WIFI\n
                    [+]  9 . CREATING A FAKE ACCESS POINT\n\n
                    [+]  0 . EXIT\n
    ''', "red" , attrs=["bold"]))

    flag = get_input()
try:
    if flag == 0 :
        print("\n\nTHANKS FOR VISITING")
        exit(0)
    elif flag == 1:
        arpspoofer.start()
    elif flag == 2:
        arp_spoof_detector.start()
    elif flag == 3 :
        print("\n\t\t\tFIRST DOING ARP SPOOFER AND THEN DNS SPOOFER\n")
        arpspoofer.start()
        dns_spoof.start()
    elif flag == 4:
        print("\n\t\t\t\tFIRST DOING ARP SPOOFER AND THEN CUT THE NETWORK\n")
        arpspoofer.start()
        net_cut.start()
    elif flag == 5:
        port_scanner.start()

    if flag > 5 :

        iface = input("ENTER YOUR WIRELESS ADAPTER WHICH SUPPORTS MONITOR MODE : ")
        mon_mode.is_monitor_mode(iface)

        if flag == 6:
            wifi_detector.start(iface)
        if flag == 7:
            deauthenticate_clients.start(iface)
        if flag == 8:
            finding_clients.start(iface)
        if flag == 9:
            fake_access_points.start(iface)

except Exception as e:
    print("SOMETHING WENT WRONG")
    print(e)




