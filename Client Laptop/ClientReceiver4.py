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
ax1 = fig.add_subplot(1,1,1)
xar = []
yar = []
zar = []

xs = []
ys = []
zs = []


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
        
def animate2(i,xs,ys):   
    xar = xar[-20:]
    yar = yar[-20:]
    ax1.clear()
    ax1.plot(xar,zar)

def Aarray (data,data1):
    num = data1  
    if num == 0:
        xs.append(data)
    elif num == 1:
        ys.append(data)
    elif num ==2:
        zs.append(data)
    
def animate(i):
    pullData = open("somefile.txt","r+").read()
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
    ax1.clear()
    ax1.plot(xar,yar)
    
def animate3(i, xs, ys):
    
    for i in range (100):
        axes = (transmit("GET"))
        axes2 = axes.split(',')
        print (axes)
        p = re.compile(r'[-+]?\d*\.\d+|\d+')
        length = 0
        data1 = 0
        for i in axes2:  
            mlist = p.findall(i)
            axes3=int_in_place(mlist)
            print(axes3)
            Aarray(axes3,data1)
            data1 = data1+1
        print ('x', xs)
        print ('y', ys)
        print ('z', zs)
        xs = xs[-20:]
        ys = ys[-20:]
        ax1.clear()
        ax1.plot(xs,ys)
##while (1):
##    for i in range (100):
##        axes = (transmit("GET"))
##        axes2 = axes.split(',')
##        print (axes)
##        p = re.compile(r'[-+]?\d*\.\d+|\d+')
##        length = 0
##        data1 = 0
##        for i in axes2:  
##            mlist = p.findall(i)
##            axes3=int_in_place(mlist)
##            print(axes3)
##            Aarray(axes3,data1)
##            data1 = data1+1
##        print ('x', xar)
##        print ('y', yar)
##        print('z', zar)
ani = animation.FuncAnimation(fig, animate3, fargs=(xs, zs), interval=5000)
plt.show()


