from scapy.all import ARP, Ether, srp

def scan(ip_range):
    print(f"[*] Scanning {ip_range}...\n")
    arp = ARP(pdst=ip_range)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether / arp

    result = srp(packet, timeout=3, verbose=0)[0]

    print("{:<20} {:<20}".format("IP Address", "MAC Address"))
    print("-" * 40)
    for sent, received in result:
        print("{:<20} {:<20}".format(received.psrc, received.hwsrc))

if __name__ == "__main__":
    target_range = input("Enter IP range (e.g. 192.168.1.0/24): ")
    scan(target_range)
