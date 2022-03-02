from tkinter import *

root = Tk()
width = 500
height = 300
def change():
    height = height_variable.get()
    width = width_variable.get()
    root.geometry(f"{width}x{height}")
root.geometry(f"{width}x{height}")

win_height = Label(root,text="Height").grid(row=0,column=0)
win_width = Label(root,text="Width").grid(row=1,column=0)

height_variable = IntVar()
width_variable = IntVar()

height_entry = Entry(root,textvariable=height_variable).grid(row=0,column=1)
width_entry = Entry(root,textvariable=width_variable).grid(row=1,column=1)

apply = Button(root,text="Apply",command=change).grid(row=2,column=0)

root.mainloop()