# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 21:16:35 2021

@author: Ivan
版權屬於「行銷搬進大程式」所有，若有疑問，可聯絡ivanyang0606@gmail.com

Line Bot聊天機器人
第四章 選單功能
多樣版組合按鈕CarouselTemplate
"""

import paho.mqtt.client as mqtt  #import the client1
import time

def on_connect(client, userdata, flags, rc):
    if rc==0:
        client.connected_flag=True #set flag
        print("connected OK")
    else:
        print("Bad connection Returned code=",rc)

mqtt.Client.connected_flag=False#create flag in class

client = mqtt.Client()             #create new instance 
client.on_connect=on_connect  #bind call back function
client.loop_start()
client.username_pw_set("Sylvia","Sylvia")
broker="120.119.157.238"
print("Connecting to broker ",broker)
client.connect(broker,1800)      #connect to broker

while not client.connected_flag: #wait in loop
    print("In wait loop")
    time.sleep(1)
print("in Main Loop")

client.loop_stop()    #Stop loop 
client.disconnect() # disconnect

