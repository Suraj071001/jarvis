from tkinter import *

root = Tk()

root.geometry("500x400")

def p1() :
    print("Button 1 is working")

def p2() :
    print("Button 2 is working")

def p3() :
    print("Button 3 is working")

def p4() :
    print("Button 4 is working")

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
button = Button(f3,fg="blue",text="Button 4",font="cas 14 bold",bg="sky blue",command=p4)
button.pack(side=LEFT,padx=10)

# todo : entry widget and grid layout
f4 = Frame(root,bg="orange",relief=SUNKEN,borderwidth=5)
f4.pack()



root.mainloop()
