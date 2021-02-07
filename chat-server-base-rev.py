import socket
import tqdm
import os
import select

# Server IP is 192.168.10.19 in Wifi: ICNL
# Server IP is 192.168.113.77 in Wifi: eduroam
# device's IP address
#SERVER_HOST = "192.168.0.6"
HEADER_LENGTH = 10
SERVER_HOST = '192.168.0.6'
SERVER_PORT = 5000
#USERS = dict()
clients = dict()

# create the server socket
# TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# bind the socket to our local address
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen()

sockets_list = [server_socket]








def receive(client_socket):
	try:
		msg_header = client_socket.recv(HEADER_LENGTH)
		if not len(msg_header):
			return False

		msg_length = int(msg_header.decode("utf-8").strip())
		return {"header": msg_header, "data": client_socket.recv(msg_length)}

	except:
		return False





while True:
	read_sockets, _, exception_sockets = select.select(sockets_list, [], sockets_list)

	for notified_socket in read_sockets:
		if notified_socket == server_socket:
			client_socket, client_address = server_socket.accept()

			user = receive(client_socket)
			if user is False:
				continue

			sockets_list.append(client_socket)

			clients[client_socket] = user

			print(f"Accepted new connection from {client_address[0]}:{client_address[1]} username: {user['data'].decode('utf-8')}")

		else:
			message = receive(notified_socket)

			if message is False:
				print(f"Closed conenction from {clients[notified_socket]['data'].decode('utf-8')}")
				sockets_list.remove(notified_socket)
				del clients[notified_socket]
				continue

			user = clients[notified_socket]
			print(f"Received message from {user['data'].decode('utf-8')}: {message['data'].decode('utf-8')}")

			for client_socket in clients:
				if client_socket != notified_socket:
					client_socket.send(user['header'] + user['data'] + message['header'] + message['data'])


	for notified_socket in exception_sockets:
		sockets_list.remove(notified_socket)
		del clients[notified_socket]







"""
"""
print(f"{SERVER_HOST}:{SERVER_PORT} SERVER is started!")

s.listen(5)
while True:
	clientsocket, address = s.accept()
	print(f"Connection from {address} has been established!")
	client.send(bytes("Welcome to the server", "utf-8"))




"""
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
""" 