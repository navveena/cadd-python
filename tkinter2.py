from tkinter import*
root=Tk()
num1=StringVar()
num2=StringVar()
num3=StringVar()
num4=StringVar()
lab1=Label(root,text="name").grid(row=0,column=1)
ent1=Entry(root,textvariable=num1).grid(row=0,column=2)
lab2=Label(root,text="rollno").grid(row=0,column=3)
ent2=Entry(root,textvariable=num2).grid(row=0,column=4)
lab3=Label(root,text="english").grid(row=1,column=2)
ent3=Entry(root,textvariable=num3).grid(row=1,column=3)
lab4=Label(root,text="CS").grid(row=2,column=2)
ent4=Entry(root,textvariable=num4).grid(row=2,column=3)

def sum(a):
    total=0
    if(a=="A"):
        total=total+100
    elif(a=="B" ):
        total=total+90
    elif(a=="C"):
         total=total+80
    return total


def f2():  
    num33=num3.get()
    num44=num4.get()
    n1=sum(num33)
    n2=sum(num44)
    total=n1+n2
    print(total)

but1=Button(root,command=f2,text="submit").grid(row=2,column=3)


root.mainloop()