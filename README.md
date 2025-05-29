# Network Device Mapper (Python + Scapy)

A lightweight Python tool that scans your local network for live devices using ARP requests.

## Features

- Maps IP to MAC addresses on the local subnet
- Uses `scapy` for low-level packet crafting
- Supports CIDR input (e.g., `192.168.1.0/24`)

## How to Use

```bash
pip install scapy
python3 network_mapper.py

if password needed - run sudo python3 network_mapper.py

enter network range when prompted

## Sample Output

[*] Scanning 192.168.1.0/24...

IP Address           MAC Address
----------------------------------------
192.168.1.1          00:11:22:33:44:55
192.168.1.10         58:ef:68:99:aa:bb
192.168.1.21         dc:a6:32:10:ff:01
