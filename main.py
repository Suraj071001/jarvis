from tkinter import *
import os
from PIL import Image,ImageTk

root = Tk()
root.geometry("600x800")
root.maxsize(800,600)
root.minsize(300,200)
root.title("My GUI with Harry")
suraj = Label(text="Images")
suraj.pack()

photo_jpg = Image.open("ship.jpg")
photo = ImageTk.PhotoImage(photo_jpg)
nitesh = Label(image=photo)
nitesh.pack()

root.mainloop()
