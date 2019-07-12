import socket
from time import sleep
import re
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import axes3d
from matplotlib import style

host = '192.168.137.10'
port = 5005
fig = plt.figure()
fig2 = plt.figure()
ax1 = fig.add_subplot(1,1,1)
ax2 = fig2.add_subplot(111,projection = '3d')
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
    ax2.plot(xar,yar,zar)
    ax2.set_xlabel('X axis')
    ax2.set_ylabel('Y axis')
    ax2.set_zlabel('Z axis')
    plt.show()
    
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

def animate(i):
    pullData = open("somefile1.txt","r+").read()
    dataArray = pullData.split('\n')
    xar = []
    yar = []
    zar = []
    for eachLine in dataArray:
        if len(eachLine)>1:
            x,y,z = eachLine.split(',')
            xar.append(float(x))
            yar.append(float(y))
            zar.append(float(z))
    print ( xar)
    ax1.clear()
    ax1.plot(xar,yar)
    
def write_file(dt,l):
    if (l <3):
        with open('somefile1.txt', 'a') as the_file:
            the_file.write(str(dt) + ',')
            ani = animation.FuncAnimation(fig, animate, interval=1000)
            plt.show()
           
    else:
        with open('somefile1.txt', 'a') as the_file:
            the_file.write(str(dt) + '\n')
##            ani = animation.FuncAnimation(fig, animate, interval=1000)
##            plt.show()
        the_file.close()

        
##    for i in range(3):
##        with open('somefile.txt', 'w') as the_file:
##            the_file.write(str(dt) + ',')
         

        

#L = [2]
while (1):
     for i in range (100):
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
    #       L.append(axes3) 
    # print (L)
            write_file(axes3,length)
        print (xar)
        print (yar)
        print(zar)
     plot3D()
