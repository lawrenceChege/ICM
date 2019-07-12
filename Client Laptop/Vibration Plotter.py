import socket
from time import sleep
import re
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import datetime as dt

host = '192.168.137.10'
port = 5005
fig = plt.figure()
fig2 = plt.figure()
ax1 = fig.add_subplot(1,1,1)
xar = []
yar = []
zar = []
Tim = []

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

def Aarray (data,data1):
    num = data1  
    if num == 0:
        xar.append(data)
    elif num == 1:
        yar.append(data)
    elif num ==2:
        zar.append(data)
        
    Tim.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
        
def animate(i,xar,Tim): 
    xar = xar[-20:]
    Tim = Tim[-20:]
    ax1.clear()
    ax1.plot(xar,Tim)
    
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('Vibration Analysis')
    plt.ylabel('X-Displacement')


    
while (1):
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
        print (xar)
        print (yar)
        print(zar)
        print (Tim)
        ani = animation.FuncAnimation(fig, animate, fargs=(xar,Tim), interval=1000)
        plt.show()
   

