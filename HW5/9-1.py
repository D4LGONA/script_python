# 9-1

from tkinter import *

def up():
    canvas.move('ball', 0, -5)
def down():
    canvas.move('ball', 0, 5)
def left():
    canvas.move('ball', -5, 0)
def right():
    canvas.move('ball', 5, 0)

window = Tk()
window.title("공 옮기기")
width = 200
height = 100
canvas = Canvas(window, bg='white', width=width, height=height)
canvas.pack()
canvas.create_oval(10, 10, 20, 20, fill='yellow',tags='ball')
frame = Frame(window)
frame.pack()
lB = Button(frame, text="좌", command=left)
lB.pack(side=LEFT)
rB = Button(frame, text="우", command=right)
rB.pack(side=LEFT)
uB = Button(frame, text="상", command=up)
uB.pack(side=LEFT)
dB = Button(frame, text="하", command=down)
dB.pack(side=LEFT)

window.mainloop()