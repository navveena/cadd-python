from tkinter import*

win=Tk()

win.geometry("750x250")


win.grid_rowconfigure(5,weight=3)
win.grid_columnconfigure(5,weight=3)

label=Label(win,text="this is a text",font=('aerial 15 bold'))
label.grid(row=30,column=0)

label=Label(win,text="this is a left text",font=('aerial 15 bold'))
label.grid(row=60,column=0)
win.mainloop()