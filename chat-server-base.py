import socket
import tqdm
import os

# Server IP is 192.168.10.19 in Wifi: ICNL
# Server IP is 192.168.113.77 in Wifi: eduroam
# device's IP address
SERVER_HOST = "192.168.113.89"
SERVER_PORT = 5001
USERS = dict()


# create the server socket
# TCP socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# bind the socket to our local address
s.bind((SERVER_HOST, SERVER_PORT))
print(f"[*] Server Starts - {SERVER_HOST}:{SERVER_PORT}")


data, addr = s.recvfrom(1024)
RCV = data.decode('utf-8')
while RCV != 'ŒEXITŒŒSERVERŒ':
	if 'ŒSEPŒ' in RCV:
		USERS[addr[0]] = RCV[:-5]
		#print(USERS)
		print(f"Clinet {addr[0]}:{addr[1]} join in this chat as NAME : {RCV[:-5]}")
	elif 'ŒEXITŒ' in RCV:
		print(f"Clinet {USERS[addr[0]]} left this chat")
		del USERS[addr[0]]
	else:
		for ip, nickname in USERS.items():
			RCV += 'ŒSEPŒ'
			RCV += nickname
			s.sendto(RCV.encode('utf-8'), addr)
		
		print(f"{USERS[addr[0]]} : {RCV.split('ŒSEPŒ')[0]}")
	data, addr = s.recvfrom(1024)
	RCV = data.decode('utf-8')

# start receiving the file from the socket
# and writing to the file stream
s.close()
