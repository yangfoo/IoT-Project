from LoginSystem.LoginSystem import *
import tkinter as tk
from tkinter import *
import os
import random
import requests
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from time import sleep

if __name__ == "__main__":
    RFID = False
    if RFID:
        relay = 24
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(relay,GPIO.IN)

        # Create a object for the RFID module
        read = SimpleMFRC522()
        list_of_files = os.listdir()
        while True:
            print("Place your Tag")
            id,Tag = read.read()
            
            id = str(id)
                    
            if id in list_of_files:
                file1 = open(id,'r')
                username = file1.read().splitlines()
                print("Welcome " + username[0])
                window = Tk()
                LoginPageRIFD(window, username[0])
                window.mainloop()             
            else:
                print("Wrong Tag!")
        
    else:
        window = Tk()
        Main(window)
        window.mainloop()
        # LoginPage(window)