'''
Simple program that connects to server by inputting IPAddress, and could chat with oneself or each other.

usage: python chat.py [address]
References: 
https://www.youtube.com/watch?v=DIPZoZheMTo

@BennyFung
'''

import socket
import threading
import sys

def help():
	print("Usage: python chat.py [address]")
	print("Open another terminal window and run the program again with your own IP to chat with yourself")

class Server:
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	connections = []
	
	def __init__(self):
		self.sock.bind(('0.0.0.0', 10000))
		self.sock.listen(1)

	def handler(self, con, address):
		while True:
			data = con.recv(1024)
			for connection in self.connections:
				connection.send(data)
			if not data:
				print(str(address[0])+ ':' + str(address[1]), "has disconnected")
				self.connections.remove(c)
				c.close()
				break

	def run(self):
		while True:
			c, a = self.sock.accept()
			cThread = threading.Thread(target=self.handler, args=(c,a))
			cThread.daemon = True
			cThread.start()
			self.connections.append(c)
			print(str(a[0])+ ':' + str(a[1]), "has connected")

class Client:
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	def send(self):
		while True:
			self.sock.send(bytes(input(""), 'UTF-8'))

	def __init__(self, address):
		self.sock.connect((address, 10000))

		inputThread = threading.Thread(target = self.send)
		inputThread.daemon = True
		inputThread.start()

		while True:
			data = self.sock.recv(1024)
			if not data:
				break
			print(address + ": " + str(data, "UTF-8"))

if (len(sys.argv) > 1):
	client = Client(sys.argv[1])
else:
	help()
	server = Server()
	server.run()