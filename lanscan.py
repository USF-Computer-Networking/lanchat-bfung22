'''
ARP Scanner to scan possible users in the network
--incomplete, still in progress
Reference: https://null-byte.wonderhowto.com/how-to/build-arp-scanner-using-scapy-and-python-0162731/ , https://securityblog.gr/1078/arp-scanning-using-python-and-scapy/

@BennyFung
'''

import socket
import threading
import sys
from scapy.all import srp,Ether,ARP,conf

def lanscan(n, ip):
	while True:
		try:
			conf.verb = 0
			ans, unans = srp(Ether(dst = "ff:ff:ff:ff:ff:ff")/ARP(pdst = ip), timeout = 2, iface = n, inter = 0.1)
			print("MAC - IP\n")
			for snd, recv in ans:
				print(recv.sprintf(r"%Ether.src% - %ARP.psrc%"))

		except KeyboardInterrupt:
			print("Scanning error\n")
			usage()
			exit()

def usage():
	print("LANSCAN\nInput network and IP\nUsage: python server.py [n] [i]")

def main():
	if len(sys.argv) != 3:
		usage()
		exit()
	else:
		n = sys.argv[1]
		ip = sys.argv[2]
		lanscan(n, ip)

main()

