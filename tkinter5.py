from tkinter import*

def selection():
    selection="you selected the option" + str(radio.get())
    label.config(text = selection)

top= Tk()

radio=StringVar()

lbl=Label(text= "your daily food chart:")
lbl.pack()
R1=Radiobutton(top,text="bread",variable=radio,value="bread",command=selection)
R1.pack()

R2=Radiobutton(top,text="chapathi",variable=radio,value="chapathi",command=selection)
R2.pack()

label=Label(top)
label.pack()

top.mainloop()