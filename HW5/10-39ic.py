from tkinter import *
from random import *
from tkinter.messagebox import *

class MainGUI:
    def verify(self):
        fourCards = [self.deck[i] % 13 + 1 for i in range(4)]
        fourCards.sort()
        ex = self.E.get() # 수식 읽어오기
        ex = ex.replace('+', ' ')
        ex = ex.replace('-', ' ')
        ex = ex.replace('*', ' ')
        ex = ex.replace('/', ' ')
        ex = ex.replace('(', ' ')
        ex = ex.replace(')', ' ')
        numbers = ex.split()
        numbers = [eval(s) for s in numbers]
        numbers.sort()

        if fourCards == numbers:
            if eval(self.E.get()) == 24:
                showinfo('정답', '맞았습니다!')
            else:
                showerror('오답', self.E.get()+'은 24점이 아닙니다')
        else:
            showerror('오답', '주어진 카드를 사용해야 합니다')

    def refresh(self):
        shuffle(self.deck) # 카드 인덱스 덱 셔플링
        for i in range(4):
            self.labelList[i]['image'] = self.imageList[self.deck[i]]

    def __init__(self):
        window = Tk()
        window.title('24점 게임')
        Button(window, text='새로고침', command=self.refresh).pack()
        self.imageList = [ PhotoImage(file='image/'+str(i)+'.gif') for i in range(1, 53) ]
        self.deck = [x for x in range(52)]
        frame1 = Frame(window)
        frame1.pack()
        self.labelList = []
        for i in range(4):
            self.labelList.append(Label(frame1, image=self.imageList[i]))
            self.labelList[i].pack(side=LEFT)

        self.refresh()
        frame2 = Frame(window)
        frame2.pack()
        Label(frame2, text='수식을 입력하세요: ').pack(side=LEFT)
        self.E = Entry(frame2)
        self.E.pack(side=LEFT)
        Button(frame2, text='확인', command=self.verify).pack(side=LEFT)

        window.mainloop()

MainGUI()