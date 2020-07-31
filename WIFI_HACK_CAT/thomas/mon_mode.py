import subprocess
import re
def is_monitor_mode(iface):
    try:
        subprocess.call(f"ifconfig {iface} down ;iw dev wlan0 set type monitor ;ifconfig wlan0 up", shell=True)
        s = subprocess.check_output("iwconfig "+ iface,shell=True , text=True)
        k = re.search("(Mode:)(.*?\s)", s)
        if k[2].strip(" ") != "Monitor":
            print("\nput your card in monitor mode and continue")
            exit(0)
    except:
        print("\n\nenter the correct interface which can support monitor mode")
        exit(0)
