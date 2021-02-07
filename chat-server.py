import socket
import os

# Server IP is 192.168.10.19 in Wifi: ICNL
# Server IP is 192.168.113.77 in Wifi: eduroam
# device's IP address
SERVER_HOST = "192.168.121.128"
SERVER_PORT = 5020
USERS = dict()

SCREEN_PORT = SERVER_PORT + 4


# create the server socket
# TCP socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# bind the socket to our local address
s.bind((SERVER_HOST, SERVER_PORT))
print(f"[*] Server Starts - {SERVER_HOST}:{SERVER_PORT}")


data, addr = s.recvfrom(1024)
#s.connect((addr[0], SCREEN_PORT))
RCV = data.decode('utf-8')


while RCV != 'ŒEXITŒŒSERVERŒ': #Server Poweroff
	if 'ŒSEPŒ' in RCV: #Connection
		print("1")
		USERS[addr[0]] = RCV[:-5]
		print(USERS)
		Inform = f"Clinet {addr[0]}:{addr[1]} join in this chat room as NAME : {RCV[:-5]}"
		print(Inform)
		InformForOthers = (f"{USERS[addr[0]]} joined this chat room").encode('utf-8')
		InformForInvolved = (f"{USERS[addr[0]]}").encode('utf-8')

		for ip, nickname in USERS.items():
			if ip != addr[0]:
				print("1-1")
				s.sendto(InformForOthers, addr)
			else:
				print("1-2")
				print(addr)
				s.sendto(InformForInvolved, addr)
				print("sended")

	elif 'ŒEXITŒ' in RCV: #Disconnection
		print("2")
		print(f"Clinet {USERS[addr[0]]} left this chat room")

		for ip, nickname in USERS.items():
			if ip == addr[0]: #involved
				print("2-1")
				s.sendto(RCV.encode(), addr)
			else:
				print("2-2")
				InformForOthers = (f"{USERS[addr[0]]} left this chat room").encode('utf-8')
				s.sendto(InformForOthers, addr)
		del USERS[addr[0]]

	else:
		print("3")
		for ip, nickname in USERS.items():
			if ip != addr[0]:
				print("3-1")
				RCV += 'ŒSEPŒ'
				RCV += nickname
				s.sendto(RCV.encode('utf-8'), addr)
			else:
				print("3-2")
				continue
		
		print(f"{USERS[addr[0]]} : {RCV.split('ŒSEPŒ')[0]}")
	data, addr = s.recvfrom(1024)
	RCV = data.decode('utf-8')

# start receiving the file from the socket
# and writing to the file stream
s.close()
