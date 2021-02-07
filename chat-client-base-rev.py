import socket, tqdm, os, time
from threading import Thread
import cursor
import select
import sys
import errno

"""
def check():
	time.sleep(0.5)
	if TXT != None:
		return
	#print("Too Slow")



SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096 # send 4096 bytes each time step

# the ip address or hostname of the server, the receiver
host = "192.168.0.6"
# the port, let's use 5001
port = 5001

# create the client socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print(f"[+] Connecting to {host}:{port}")
s.connect((host, port))
print("[+] Connected.")

USER = input("[@] Enter Your User Name(Nickname): ")
USER += "ŒSEPŒ"
s.sendto(USER.encode('utf-8'), (host, port))

# send the filename and filesize
#s.send(f"{filename}{SEPARATOR}{filesize}".encode())
while True:
	TXT = None
	Thread(target = check).start()
	TXT = input(f"{USER[:-5]}: ")
	try:
		s.sendto(TXT.encode('utf-8'), (host, port))
		if "ŒEXITŒ" in TXT:
			print("[+] Disconnected.")
			break
	except:
		pass

	try:
		######## Coding, Implement####
		data, addr = s.recvfrom(1024)
		data = data.decode('utf-8')
		DATA = data.split('ŒSEPŒ')
		print(DATA)
		cursor.delete_last_line()
		print(f"{DATA[1]}: {DATA[0]}")
	except:
		pass

s.close()
"""



HEADER_LENGTH = 10
SERVER_HOST = '10.150.5.109'
SERVER_PORT = 5000
#USERS = dict()
clients = dict()


my_username = input("Username: ")
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_HOST, SERVER_PORT))
client_socket.setblocking(False)

username = my_username.encode("utf-8")
username_header = f"{len(username):<{HEADER_LENGTH}}".encode("utf-8")
client_socket.send(username_header+username)

while True:
	message = input(f"{my_username} > ")

	if message:
		message = message.encode("utf-8")
		message_header = f"{len(message):<{HEADER_LENGTH}}".encode("utf-8")
		client_socket.send(message_header+message)


	try:
		while True:
			#receive things
			username_header = client_socket.recv(HEADER_LENGTH)
			if not len(username_header):
				print("connection closed by the server")
				sys.exit()

			username_length = int(username_header.decode("utf-8").strip())
			username = client_socket.recv(username_length).decode("utf-8")

			message_header = client_socket.recv(HEADER_LENGTH)
			message_length = int(message_header.decode("utf-8").strip())
			message = client_socket.recv(message_length).decode("utf-8")

			print(f"{username} > {message}")

	except IOError as e:
		if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
			print("Reading Error", str(e))
			sys.exit()
		continue

	except Exception as e:
		print("General error", str(e))
		sys.exit()