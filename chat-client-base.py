import socket, tqdm, os, time
from threading import Thread

import cursor

def check():
	time.sleep(0.5)
	if TXT != None:
		return
	#print("Too Slow")



SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096 # send 4096 bytes each time step

# the ip address or hostname of the server, the receiver
host = "192.168.113.89"
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
		cursor.delete_last_line()
		print(f"{DATA[1]}: {DATA[0]}")
	except:
		pass

s.close()
