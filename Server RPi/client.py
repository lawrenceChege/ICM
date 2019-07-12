#! /usr/bin/python3
import requests
from Transmission_2 import ADXL345
import re
import json
from collections import deque
import time
import datetime
import pandas as pd

X = deque(maxlen=20)
X.append(1)
Y = deque(maxlen=20)
Y.append(1)
Z = deque(maxlen=20)
Z.append(1)


def getData():
    adxl345 = ADXL345()
    axes = adxl345.getAxes(True)
##print ((axes['x']))
##print ((axes['y']))
##print ((axes['z']))

    reply = dict(axes)
    return reply

def populate (data,data1):
    num = data1  
    if num == 0:
        Z.append(data)
    elif num == 1:
        X.append(data)
    elif num ==2:
        Y.append(data)

def float_in_place(data_list):
    data_list[0] = float(data_list[0])
    return data_list[0]

def match_float():
    data_string = getData()
    data_s = data_string.split(',')
    reg = re.compile(r'[-+]?\d*\.\d+|\d+')
    counter = 0
    for i in data_s:
        data_datum = reg.findall(i)
        data_floats = float_in_place(data_datum)
        
        populate(data_floats, counter)
        counter = counter + 1
        #print (data_floats)
        
def json_it(data_list):
    data_list = list(data_list)
    return json.dumps(data_list)


def send_req(data):
    
    #data_json = json.dumps(data)
##    response = requests.post('https://sheltered-coast-93272.herokuapp.com',
##                         json=data)
##    #print ("data:", data_json)
##    
##    if response.ok:
##        print(response.json())

    try:
        response = requests.post('https://sheltered-coast-93272.herokuapp.com',
                         json=data)
        print ("data:", data)
        print ("Data Uploaded")
    except requests.exceptions.RequestException as e:
        print (e)
        

def get_time():
    d_time = datetime.datetime.now()
    d_t = d_time.strftime('%Y-%m-%d %H:%M:%S')
    d_d = d_time.strftime('%A')
    time_dict = {'timestamp': d_t, 'day': d_d}
    return time_dict

def write_to_file(data):
    x = []
    y = []
    z = []

    for key, value in data.items():
        if key == 'x':
            x.append(value)
        if key == 'y':
            y.append(value)
        if key == 'z':
            z.append(value)

    date_c = get_time()
    date_t = pd.Timestamp(date_c['timestamp'])
    raw_data = {'timestamp': date_t, 'day': date_c['day'], 'x-axis': x, 'y-axis': y, 'z-axis': z}

    d_frame = pd.DataFrame(raw_data, columns = ['timestamp', 'day', 'x-axis', 'y-axis', 'z-axis'])
    d_frame.to_csv('/home/pi/Desktop/Accelerometer/histogram.csv', mode='a', header=False, index='Unnamed: 0')
    print("File Logged")
        
while True:
    data = getData()
    #print(type(data))
    #match_float()
    #print ("x:", list(X))
    #print ("y:", list(Y))
    #print ("z:", list(Z))
    #x = json_it(X)
    #y = json_it(Y)
    #print("x:", x)
    #print("y:", y)
    
    #dt = json_it(data)
    write_to_file(data)
    send_req(data)
    time.sleep(2)
    
    #print(str(dt))
    #print(data)
