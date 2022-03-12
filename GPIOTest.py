#!/usr/bin/env python2.7  
# script by Alex Eames https://raspi.tv/  
# https://raspi.tv/2013/how-to-use-interrupts-with-python-on-the-raspberry-pi-and-rpi-gpio  
import RPi.GPIO as GPIO
from guizero import App
from guizero import Text
from pubnub.callbacks import SubscribeCallback
from pubnub.enums import PNStatusCategory
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub
import time
import os
import socket

pnconfig = PNConfiguration()
pnconfig.publish_key = 'pub-c-d8a36fd5-e1a3-400c-9fa8-974ace1a8d37'
pnconfig.subscribe_key = 'sub-c-a623694c-4c89-11ea-94fd-ea35a5fcc55f'
pnconfig.ssl = True
pubnub = PubNub(pnconfig)
def my_publish_callback(envelope, status):
    # Check whether request successfully completed or not
    if not status.is_error():
        pass
class MySubscribeCallback(SubscribeCallback):
    def presence(self, pubnub, presence):
        pass
    def status(self, pubnub, status):
        pass
    def message(self, pubnub, message):
        print ("from device 2: ")
        print(message.message)
pubnub.add_listener(MySubscribeCallback())
pubnub.subscribe().channels("chan-1").execute()


ButtonCount = 0;
WindowText = "NAME"
app = App(title="Hello world", width = 600, height = 300)
Name = Text(app, text=WindowText, size=80, font="Times New Roman", color="red", width = "fill", height = "fill")


def interrupt(channel):
    global ButtonCount
    global Name
    global pubnub
    print("Button Pressed!");
    ButtonCount = ButtonCount + 1;
    Name.value = "ButtonPressed!"
    pubnub.publish().channel("chan-1").message(str("ButtonPressed!")).pn_async(my_publish_callback)

GPIO.setmode(GPIO.BCM)  
  
# GPIO 17 set up as input. It is pulled up to stop false signals  
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)  
  

input("Press Enter when ready\n>")  



GPIO.add_event_detect(17, GPIO.FALLING, callback=interrupt, bouncetime=500) 

print("GPIO Interrupt Attached");


app.display()






try:
    while(ButtonCount < 10):
        pass
except KeyboardInterrupt:
     print("Exiting");
finally:
    GPIO.cleanup()           # clean up GPIO on normal exit
    print("GPIO Cleaned up");