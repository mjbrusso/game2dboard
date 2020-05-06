import gui2darray
from tkinter import *

root = Tk()
frame = Frame(root, bg="white")
frame.pack()

c1 = gui2darray.Cell(frame)
c1.bg = "green"

c2 = gui2darray.Cell(frame)
c2.bg = "blue"
c2.image = "img/12.png"

root.mainloop()
