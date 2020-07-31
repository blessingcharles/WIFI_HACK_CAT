import socket
from threading import Thread
def port_scanner(ip , port):
    s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.settimeout(1)
    if s.connect_ex((ip , port)):
        print(f"closed port :{port}")
    else:
        print(f"\n[+]port opened ------> port:{port}[+]\n")
def start():
    ip = input("\nenter the host ip to scan: ")
    n = int(input("\npress 0 to scan for all ports or enter how many ports to scan :"))
    if n == 0:
        print(f"\t\t\t\t\t\t\t[+]SCAN RESULTS FOR   {ip}[+]")
        for port in range(50,60):
            port_scanner(ip,port)
    else :
        ports = []
        for i in range(n):
            port = input(f"enter the {n+1} port :")
            ports.append(port)
        for port in ports:
            port_scanner(ip , int(port))

