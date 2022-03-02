"""todo : GUI for making list of data"""
from tkinter import *

root = Tk()

root.geometry("500x400")

def data() :
    print(f"{user.get()} : {sport.get()}")
    with open("cricket.txt","a") as f :
        f.write(f"{user.get()} : {sport.get()}\n")

Label(text="Username",bg="white",relief=SUNKEN,borderwidth=1).grid(row=0,column=0)
Label(text="Sport",bg="white",relief=SUNKEN,borderwidth=1,padx=12.5).grid(row=1,column=0)

user = StringVar()
sport = StringVar()

username = Entry(textvariable=user,relief=SUNKEN,borderwidth=1).grid(row=0,column=1)
sportname = Entry(textvariable=sport,relief=SUNKEN,borderwidth=1).grid(row=1,column=1)

submit = Button(text="Submit",fg="red",relief=SUNKEN,borderwidth=3,command=data).grid(row=2,column=0)


root.mainloop()