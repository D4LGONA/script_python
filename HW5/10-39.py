from tkinter import *
import tkinter.simpledialog
import random
class MainGUI:
    def check(self):
        fourCards=[]
        for i in range(4):
            fourCards.append(self.index[i] % 13 + 1)
        fourCards.sort()
        ex = self.answer.get()
        ex = ex.replace('+', ' ')
        ex = ex.replace('-', ' ')
        ex = ex.replace('*', ' ')
        ex = ex.replace('/', ' ')
        ex = ex.replace('(', ' ')
        ex = ex.replace(')', ' ')
        numbers = [eval(i) for i in ex.split()]
        numbers.sort()
        if fourCards == numbers:
            if eval(self.answer.get()) == 24:
                tkinter.messagebox.showinfo("정답", "정답입니다!")
            else:
                tkinter.messagebox.showinfo("오답", self.answer.get()+"는 24가 아닙니다.")
        else:
            tkinter.messagebox.showinfo("오답", "보여지는 카드를 사용해야 합니다.")



    def reset(self):
        random.shuffle(self.index)
        for i in range(4):
            self.labelList[i]['image'] = self.imageList[self.index[i]]

    def __init__(self):
        window = Tk()
        window.title('24점 게임')
        self.index = [x for x in range(52)]
        self.imageList = []
        for i in range(1, 53):
            self.imageList.append(PhotoImage(file='image/'+str(i)+'.gif'))
        frame1 = Frame(window)
        frame1.pack()
        Button(frame1, text='새로고침',command=self.reset).pack()
        frame2 = Frame(window)
        frame2.pack()
        self.labelList = []
        for i in range(4):
            self.labelList.append(Label(frame2, image=self.imageList[i]))
            self.labelList[i].pack(side=LEFT)
        self.reset()
        frame3 = Frame(window)
        frame3.pack()
        Label(frame3,text='수식을 입력하세요: ').pack(side=LEFT)
        self.answer = StringVar()
        Entry(frame3, textvariable=self.answer).pack(side=LEFT)
        Button(frame3,text='확인',command=self.check).pack(side=LEFT)

        window.mainloop()

MainGUI()