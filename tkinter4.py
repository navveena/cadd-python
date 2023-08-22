from tkinter import*

win=Tk()

win.geometry("750*250")


win.grid_rowconfig(5,weight=3)
win.grid_columnconfig(5,weight=3)

label=Label(win,text="this is a text",font=('aerial 15 bold'))
label.grid(row=30,column=0)

label=Label(win,text="this is a left text",font=('aerial 15 bold'))
label.grid(row=60,column=0)
win.mainloop()