from tkinter import *
import random

class MainGUI:
    def random_words(self):
        self.hist = [0 for _ in range(26)]
        for i in range(1000):
            rnd = random.randint(0,25)
            self.hist[rnd] += 1

    def show(self):
        self.random_words()
        self.canvas.delete("all")
        width = int(self.canvas['width'])
        height = int(self.canvas['height'])
        maxCounts = max(self.hist)
        heightBar = height * 0.75
        widthBar = width - 20
        for i in range(26):
            x0 = 10 + i * widthBar / 26
            y0 = height - 20
            x1 = 10 + (i + 1) * widthBar / 26
            y1 = height - heightBar * self.hist[i] / maxCounts - 20
            self.canvas.create_rectangle(x0, y0, x1, y1)
            x_text = (x0 + x1) / 2
            y_text = y1 - 10
            self.canvas.create_text(x_text, y_text, text=str(self.hist[i]), font=("Helvetica", 8))
            self.canvas.create_text(i * widthBar / 26 + 10 + 0.5 * widthBar / 26, height - 10, text=chr(i + ord('a')))

    def __init__(self):
        self.window = Tk()
        self.window.title("문자의 개수 세기")
        frame1 = Frame(self.window)
        frame1.pack()
        self.canvas = Canvas(self.window, bg='white', width=400, height=200)
        self.canvas.pack()
        Button(self.window, text='히스토그램 출력', command=self.show).pack()

ML = MainGUI()
ML.window.mainloop()
