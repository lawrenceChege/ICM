from mpl_toolkits.mplot3d import axes3d
from matplotlib import style
import matplotlib.pyplot as plt
import numpy as np
import socket
from time import sleep
import re

#style.use('fivethirtyeitght')

host = '192.168.137.10'
port = 5005
fig = plt.figure()
ax2 = fig.add_subplot(111,projection = '3d' )

xar = []
yar = []
zar = []

def plt3D():
    pullData = open("somefile1.txt","r+").read()
    dataArray = pullData.split('\n')
  
    for eachLine in dataArray:
        if len(eachLine)>1:
            x,y,z = eachLine.split(',')
            xar.append(float(x))
            yar.append(float(y))
            zar.append(float(z))

    
def setupSocket():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    return s

def sendReceive(s, message):
    s.send(str.encode(message))
    reply = s.recv(1024)
    print("We have received a reply")
    s.close()
    reply = reply.decode('utf-8')
    return reply

def transmit(message):
    s = setupSocket()
    response = sendReceive(s, message)
    return response

def int_in_place(mlist):
    mlist[0] = float(mlist[0])
    return mlist[0]
def write_file(dt,l):
    if (l <3):
        with open('somefile1.txt', 'a') as the_file:
            the_file.write(str(dt) + ',')
           
    else:
        with open('somefile1.txt', 'a') as the_file:
            the_file.write(str(dt) + '\n')
        the_file.close()
while (1):
    for i in range  (5):
         for i in range (10):
            axes = (transmit("GET"))
            axes2 = axes.split(',')
            print (axes)
            p = re.compile(r'[-+]?\d*\.\d+|\d+')
            length = 0
            for i in axes2:  
                mlist = p.findall(i)
                axes3=int_in_place(mlist)
                print((axes3))
                length+=1
                write_file(axes3,length)
            print (xar)
            print (yar)
            print(zar)
            plt3D()
    
    plt.show()

