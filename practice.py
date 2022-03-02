from tkinter import *

root = Tk()

root.geometry("600x600")

def getvalue() :
    print(f"Username is : {uservalue.get()}")
    print(f"User password is : {passvalue.get()}")
    print(checkboxvalue.get())

def p1() :
    print("Button 1 is working")

def p2() :
    print("Button 2 is working")

def p3() :
    print("Button 3 is working")

def p4(event) :
    print(f"Button 4 is working {event.x} and {event.y}")

f1 =Frame(root,bg="green",relief=SUNKEN,borderwidth=5)
f1.pack(side=LEFT,fill="y")

label = Label(f1,text="frame 1",font="cas 23 bold",bg="light green")
label.pack()
label = Label(f1,text="frame 2",font="cas 23 bold",bg="light green")
label.pack(pady=6)
label = Label(f1,text="frame 3",font="cas 23 bold",bg="light green")
label.pack()

f2 = Frame(root,bg="sky blue",relief=SUNKEN,borderwidth=5)
f2.pack(side=TOP,fill=X)
label = Label(f2,text="heading",font="cas 23 bold",bg="white")
label.pack()
label = Label(f2,text="sub heading 1",font="cas 10 bold",bg="yellow")
label.pack(side=TOP,anchor="nw",pady=6)
label = Label(f2,text="sub heading 2",font="cas 10 bold",bg="yellow")
label.pack(side=TOP,anchor="nw",pady=6)
label = Label(f2,text="sub heading 3",font="cas 10 bold",bg="yellow")
label.pack(side=TOP,anchor="nw",pady=6)
label = Label(f2,text="sub heading 4",font="cas 10 bold",bg="yellow")
label.pack(side=TOP,anchor="nw",pady=6)

#todo : Botton
f3 = Frame(root,bg="purple",relief=SUNKEN,borderwidth=5)
f3.pack(fill=X)

button = Button(f3,fg="blue",text="Button 1",font="cas 14 bold",bg="sky blue",command=p1)
button.pack(side=LEFT,padx=10)
button = Button(f3,fg="blue",text="Button 2",font="cas 14 bold",bg="sky blue",command=p2)
button.pack(side=LEFT,padx=10)
button = Button(f3,fg="blue",text="Button 3",font="cas 14 bold",bg="sky blue",command=p3)
button.pack(side=LEFT,padx=10)
button = Button(f3,fg="blue",text="Button 4",font="cas 14 bold",bg="sky blue")
button.pack(side=LEFT,padx=10)

button.bind("<Button-1>",p4)

# todo : entry widget and grid layout
f4 = Frame(root,bg="orange",relief=SUNKEN,borderwidth=5)
f4.pack(side=TOP,fill=X)

user = Label(f4,text="Username",bg="white")
user.grid(row=0,column=0)
password = Label(f4,text="Password",bg="white",padx=2.25)
password.grid(row=1,column=0)

uservalue = StringVar()
passvalue = StringVar()
checkboxvalue = IntVar()

userentry = Entry(f4,textvariable=uservalue,bg="white").grid(row=0,column=1)
passentry = Entry(f4,textvariable=passvalue,bg="white").grid(row=1,column=1)

check_box = Checkbutton(f4,text="Check here if :       ",variable=checkboxvalue).grid(row=2,column=1)
check_label = Label(f4,text="You want to save your username and password").grid(row=2,column=2)

submit = Button(f4,text="Submit",bg="white",relief=SUNKEN,borderwidth=3,padx=35,command=getvalue).grid(row=3,column=1)

f5 = Frame(root,bg="blue",relief=SUNKEN,borderwidth=5)
f5.pack(side=TOP,fill=X)

Label(f5,text="suraj").pack()

can_widget = Canvas(f5,width=200,height=200)
can_widget.pack()
# can_widget.create_line(0,0,200,200)
# can_widget.create_arc(0,0,200,200)
can_widget.create_polygon(100,100,30,60,200,200,fill="green")


root.mainloop()
