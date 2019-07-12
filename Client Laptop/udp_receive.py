import socket
from Transmission_2 import ADXL345

UDP_IP = "192.168.137.200"
UDP_PORT = 5005
print "test 0"
sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.connect((UDP_IP, UDP_PORT))
print "test 1"
while True:
  print "test 2"
  data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
  print"test 3"
  print "received message", data
