import math
import numpy as np
from tkinter import *

BACKGROUND = "#4b3832"
FOREGROUND = "#fff4e6"
TEXT = "#3c2f2f"

def convert(s):
    # initialization of string to ""
    new = ""
    # traverse in the string
    for x in s:
        new += x
    # return string
    return new

def CaesarDecryption(realText, step):
	outText = []
	cryptText = []
	uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
	symbol = ['~','!','@','#','$','%','^','&','*','(',')','-','_','=','+','{','}','[',']','|',':','/','?',',','.','<','>',' ']
	for eachLetter in realText:
		if eachLetter in uppercase:
			index = uppercase.index(eachLetter)
			crypting = (index - step) % 26
			cryptText.append(crypting)
			newLetter = uppercase[crypting]
			outText.append(newLetter)
		elif eachLetter in lowercase:
			index = lowercase.index(eachLetter)
			crypting = (index - step) % 26
			cryptText.append(crypting)
			newLetter = lowercase[crypting]
			outText.append(newLetter)
		elif eachLetter in number:
			index = number.index(eachLetter)
			crypting = (index - step) % 10
			cryptText.append(crypting)
			newLetter = number[crypting]
			outText.append(newLetter)
		elif eachLetter in symbol:
			index = symbol.index(eachLetter)
			crypting = (index - step) % 28
			cryptText.append(crypting)
			newLetter = symbol[crypting]
			outText.append(newLetter)	
	return convert(outText)

def MirrorDecryption(string):
  translated = '' #cipher text is stored in this variable
  i = len(string) - 1

  while i >= 0:
    translated = translated + string[i]
    i = i - 1
  return translated    

def Hybird_decryption(string, step = 3):
  Decrypted3 = MirrorDecryption(string)
  Decrypted4 = CaesarDecryption(Decrypted3, step)
  print("After Decryption  :" + Decrypted4)
  return (Decrypted4)

# window = Tk()

# window.resizable(False, False)

# window.title("Decryption Window")
# window.configure(bg = BACKGROUND)

# window_width = 500
# window_height = 250

# # get the screen dimension
# screen_width = window.winfo_screenwidth()
# screen_height = window.winfo_screenheight()

# # find the center point
# center_x = int(screen_width/2 - window_width / 2)
# center_y = int(screen_height/2 - window_height / 2)

# window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

# lbl = Label(window, text="Encrypted Text :",bg =BACKGROUND, fg=FOREGROUND, font=("Calibri", 13))

# lbl.grid(column=0, row=0)

# txt = Entry(window,width=40,bg = FOREGROUND)

# txt.grid(column=1, row=0)

# fodder1 = Label(window, text="", bg=BACKGROUND)
# fodder1.grid(column=0, row=3)
# # fodder2 = Label(window, text="")
# # fodder2.grid(column=0, row=3)

# space = Label(window, text="", bg=BACKGROUND, fg=FOREGROUND,font=("Calibri", 13))

# space.grid(column=1, row=3)

# def clicked():
#     decryption = txt.get()
#     encryption = Hybird_decryption(decryption) 
#     space.configure(text= "The Decrypted Text is :" + encryption)

# btn = Button(window, text="Decrypt", height="2", width="16", bg=BACKGROUND, fg=FOREGROUND, command=clicked)

# btn.grid(column=0, row=1)

# window.mainloop()

