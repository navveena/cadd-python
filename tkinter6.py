from tkinter import*
root=Tk()
canvas_width=800
canvas_height=600


can_widget=Canvas(root,width=canvas_width,height=canvas_height)
can_widget.pack()

points=[120,60,130,130,160,0,120]

can_widget.create_polygon(points,ouline='green',fill='blue',width=4)

root.mainloop()
