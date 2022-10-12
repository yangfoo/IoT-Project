from LoginSystem.LoginSystem import *
import tkinter as tk
from tkinter import *
import os
import random
import requests

if __name__ == "__main__":
    RFID = True
    if RFID:
        window = Tk()
        LoginPageRIFD(window, 'jy')
        window.mainloop()
    else:
        window = Tk()
        Main(window)
        window.mainloop()
        # LoginPage(window)