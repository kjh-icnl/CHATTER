import socket, os, time
from threading import Thread
import cursor


SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096 # send 4096 bytes each time step

# the ip address or hostname of the server, the receiver
host = "192.168.121.128"
# the port, let's use 5001
port = 5020

# create the client socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)



#print(f"[+] Connecting to {host}:{port}")
#s.connect((host, port))
#print("[+] Connected.")

#USER = input("[@] Enter Your User Name(Nickname): ")
USER = input(">")
USER += "ŒSEPŒ"
s.sendto(USER.encode('utf-8'), (host, port))

# send the filename and filesize
#s.send(f"{filename}{SEPARATOR}{filesize}".encode())
while True:
	TXT = None
	#Thread(target = check).start()
	#TXT = input(f"{USER[:-5]}: ")
	TXT = input("SEND> ")

	s.sendto(TXT.encode('utf-8'), (host, port))
	if "ŒEXITŒ" in TXT:
		#print("[+] Disconnected.")
		break
	cursor.delete_last_line()

	"""
	while True:
		try:
			s.settimeout(0.1)
			data, addr = s.recvfrom(1024)
			s.timeout(None)

			data = data.decode('utf-8')
			DATA = data.split('ŒSEPŒ')
			#cursor.delete_last_line()
			print(f"{DATA[1]}: {DATA[0]}")

		except:
			cursor.delete_last_line()
			TXT = input(f"{USER[:-5]}: ")
			print("PASSED")
	"""
	
s.close()
