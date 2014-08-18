#!/usr/bin/env python3

import socket

def main():
	sock=socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
	try:
		# Getting Current Network Interface
		host=socket.gethostbyname((host=sys.argv[1]))
		sock.bind(host,0))
	except:
		raise socket.error("Invalid Address !")
	

	sock.close()

if __name__=='__main__':
	main()

		
