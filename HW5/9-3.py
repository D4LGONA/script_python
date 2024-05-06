# 9-3
from tkinter import *

width = 300
height = 50

class MainGUI:
    def display(self):
        self.canvas.delete('shape')
        if self.v.get() == 1:
            shape = self.canvas.create_rectangle(width / 2 - width * 0.4, height / 2 - height * 0.4,
                                                 width / 2 + width * 0.4, height / 2 + height * 0.4, tags='shape')
        elif self.v.get() == 2:
            shape = self.canvas.create_oval(width / 2 - width * 0.4, height / 2 - height * 0.4,
                                            width / 2 + width * 0.4, height / 2 + height * 0.4, tags='shape')
        if self.filled.get() != 1:
            self.canvas.itemconfig(shape, fill='')
        else:
            self.canvas.itemconfig(shape, fill='blue')

    def __init__(self):
        self.window = Tk()
        self.window.title("라디오 버튼과 체크 버튼")
        self.canvas = Canvas(self.window, bg='white', width=width, height=height)
        self.canvas.create_rectangle(width / 2 - width * 0.4, height / 2 - height * 0.4,
                                     width / 2 + width * 0.4, height / 2 + height * 0.4, tags='shape')
        self.canvas.pack()
        frame = Frame(self.window)
        frame.pack()
        self.v = IntVar()
        Radiobutton(frame, text='직사각형', variable=self.v, value=1, command=self.display).pack(side=LEFT)
        Radiobutton(frame, text='타원', variable=self.v, value=2, command=self.display).pack(side=LEFT)
        self.filled = IntVar()
        Checkbutton(frame, text='채우기', variable=self.filled, command=self.display).pack(side=LEFT)

ML = MainGUI()
ML.window.mainloop()