import socket, os, time
from threading import Thread
import cursor


SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096 # send 4096 bytes each time step

# the ip address or hostname of the server, the receiver
SERVER_HOST = "192.168.121.128"
SERVER_PORT = 5020

SCREEN_HOST = "192.168.121.128"
SCREEN_PORT = 5024


# create the client socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((SCREEN_HOST, SCREEN_PORT))


#print(f"[+] Connecting to {SERVER_HOST}:{SERVER_PORT}")
#s.connect((SERVER_HOST, SERVER_PORT))
#print("[+] Connected.")


#print("[@] Enter Your User Name(Nickname): ")
#USER = input("[@] Enter Your User Name(Nickname): ")
#USER += "ŒSEPŒ"
#s.sendto(USER.encode('utf-8'), (host, port))

data, addr = s.recvfrom(1024)
RCV = data.decode('utf-8')

cursor.delete_last_line()
print(f"[@] Enter Your User Name(Nickname): {RCV[:-5]}")

#s.send(f"{filename}{SEPARATOR}{filesize}".encode())
while True:
	data, addr = s.recvfrom(1024)
	RCV = data.decode('utf-8')
	try:
		DATA = data.split('ŒSEPŒ')
	except:
		pass

	if 'ŒEXITŒ' in DATA[0]:
		print("[+] Disconnected.")
		break
	elif len(DATA) == 2:
		print(f"{DATA[1]}: {DATA[0]}")
	elif len(DATA) == 1:
		print(DATA)
	
s.close()
