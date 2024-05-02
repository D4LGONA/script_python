from tkinter import *
import random
from tkinter import messagebox

class MainGUI:

    def draw(self):
        length = len(self.nums)
        self.canvas.delete("all")
        width = int(self.canvas['width'])
        height = int(self.canvas['height'])
        maxCounts = max(self.nums)
        heightBar = height * 0.75
        widthBar = width - 20
        for i in range(length):
            x0 = 10 + i * widthBar / length
            y0 = height - 20
            x1 = 10 + (i + 1) * widthBar / length
            y1 = height - heightBar * self.nums[i] / maxCounts - 20
            if i == self.current:
                self.canvas.create_rectangle(x0, y0, x1, y1, fill='blue')
            else:
                self.canvas.create_rectangle(x0, y0, x1, y1)
            x_text = (x0 + x1) / 2
            y_text = y1 - 10
            self.canvas.create_text(x_text, y_text, text=str(self.nums[i]), font=("Helvetica", 8))

    def reset(self):
        self.nums = [i for i in range(1, 21)]
        random.shuffle(self.nums)
        self.current = -1
        self.draw()


    def next(self):
        key = int(self.key.get())
        if key == self.nums[self.current]:
            messagebox.showinfo("탐색 성공", f" {key}는 {self.current}번째에 있습니다.")
            return
        if key > 20 or key < 1:
            messagebox.showinfo("탐색 실패", f"{key}는 범위를 벗어납니다. 1~20의 숫자를 입력하세요.")
            return

        self.current += 1
        self.draw()



    def __init__(self):
        self.window = Tk()
        self.window.title("선형 검색 애니메이션")
        self.canvas = Canvas(self.window, bg='white', width=400, height=200)
        self.canvas.pack()
        frame = Frame(self.window)
        frame.pack()
        Label(frame, text='키를 입력하세요: ').pack(side=LEFT)
        self.key = IntVar()
        Entry(frame, textvariable=self.key, justify=RIGHT,width=3).pack(side=LEFT)
        Button(frame, text='다음단계', command=self.next).pack(side=LEFT)
        Button(frame, text='재설정', command=self.reset).pack(side=LEFT)
        self.current = -1
        self.reset()


ML = MainGUI()
ML.window.mainloop()
