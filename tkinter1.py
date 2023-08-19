from tkinter import*
root=Tk()
user1=StringVar()
def f2():
    user11=user1.get()
    if user11=="navveena":
        print("welcome")
    else:
        print("wrong user")
def f1():
    user1.set("")
ent1=Entry(root,textvariable=user1).pack()
but1=Button(root,command=f1,text="clear").pack()
but2=Button(root,command=f2,text="clickme").pack()
root.mainloop()
