import socket
from Transmission_2 import ADXL345

host = ''
port = 5005

storedValue = "Test Message"

def setupServer():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket created.")
    try:
        s.bind((host, port))
    except socket.error as msg:
        print(msg)
    print("Socket bind comlete.")
    return s

def setupConnection():
    s.listen(1) # Allows one connection at a time.
    conn, address = s.accept()
    print("Connected to: " + address[0] + ":" + str(address[1]))
    return conn

def GET():
    adxl345 = ADXL345()
    axes = adxl345.getAxes(True)
   # print (("ADXL345 on address 0x%x:") % (adxl345.address))
##    print (("x = %.3fG") % ( axes['x'] ))
##    print (("y = %.3fG") % ( axes['y'] ))
##    print (("z = %.3fG") % ( axes['z'] ))
    print (( axes['x'] ))
    print (( axes['y'] ))
    print (( axes['z'] ))
    reply = str(axes)
    return reply

def dataTransfer(conn):
    # A big loop that sends/receives data until told not to.
    while True:
        # Receive the data
        data = conn.recv(1024) # receive the data
        data = data.decode('utf-8')
        # Split the data such that you separate the command
        # from the rest of the data.
        dataMessage = data.split(' ', 1)
        command = dataMessage[0]
        if command == 'GET':
            reply = GET()
        else:
            reply = 'Unknown Command'
        # Send the reply back to the client
        conn.sendall(str.encode(reply))
        print("Data has been sent!")
    conn.close()
        

s = setupServer()

while True:
    try:
        conn = setupConnection()
        dataTransfer(conn)
    except:
        print("Exception routine triggered")
        continue
