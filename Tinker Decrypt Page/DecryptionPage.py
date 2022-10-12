import tkinter as tk
from PIL import ImageTk, Image

root = tk.Tk()

root.title('Tkinter Window Demo')
root.geometry('600x400+50+50')

message = tk.Label(root, text="Hello, World!")
message.pack()

root.mainloop()