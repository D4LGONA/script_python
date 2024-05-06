from tkinter import *

class MainGui:
    def check(self):
        for i in range(3): # 각 행과 열에 대해서 3개가 연속인가?
            ch = self.matrix[i][0]['text']
            if ch != ' ' and ch == self.matrix[i][1]['text'] and ch == self.matrix[i][2]['text']:
                return ch # 빙고가 되면 해당하는 x/o를 리턴한다
            ch = self.matrix[0][i]['text']
            if ch != ' ' and ch == self.matrix[1][i]['text'] and ch == self.matrix[2][i]['text']:
                return ch # 빙고가 되면 해당하는 x/o를 리턴한다
        # 주대각선 검사
        ch = self.matrix[0][0]['text']
        if ch != ' ' and ch == self.matrix[1][1]['text'] and ch == self.matrix[2][2]['text']:
            return ch  # 빙고가 되면 해당하는 x/o를 리턴한다

        ch = self.matrix[0][2]['text']
        if ch != ' ' and ch == self.matrix[1][1]['text'] and ch == self.matrix[2][0]['text']:
            return ch  # 빙고가 되면 해당하는 x/o를 리턴한다

        return " " # 빙고가 안됨

    def pressed(self, r, c):
        if not self.done and self.matrix[r][c]['text'] == ' ':
            if self.turn:
                self.matrix[r][c]['image'] = self.imageX
                self.matrix[r][c]['text'] = 'x'
            else:
                self.matrix[r][c]['image'] = self.imageO
                self.matrix[r][c]['text'] = 'o'
            self.turn = not self.turn

            ch = self.check()
            if ch != ' ':
                self.done = True
                self.explain.set(ch+"가 이겼습니다!")
            else:
                if self.turn:
                    self.explain.set("플레이어 x의 차례!")
                else:
                    self.explain.set("플레이어 o의 차례!")


    def refresh(self):
        self.done = False
        self.turn = True
        for i in range(3):
            for j in range(3):
                self.matrix[i][j]['image'] = self.imageE
                self.matrix[i][j]['text'] = " "
        self.explain.set("플레이어 x의 차례!")

    def __init__(self):
        self.turn = True # tf 토글, xo번갈아가면서 실행
        self.done = False # 종료되었나?
        window = Tk()
        window.title('Tic-Tac-Toe')
        frame = Frame(window)
        frame.pack()
        self.matrix = [] # 3x3 격자

        # photoimage 3개를 먼저 읽어오기
        self.imageX = PhotoImage(file='resources/x.gif')
        self.imageO = PhotoImage(file='resources/o.gif')
        self.imageE = PhotoImage(file='resources/empty.gif')

        for r in range(3):
            self.matrix.append([]) # 빈 리스트 추가
            for c in range(3):
                self.matrix[r].append(Button(frame, image=self.imageE, text=' ',
                             command=lambda row=r, col=c: self.pressed(row, col),
                             bd=0, highlightthickness=0)) # 람다함수를 이용하는것
                self.matrix[r][c].grid(row=r, column=c)

        frame1 = Frame(window)
        frame1.pack()
        self.explain = StringVar()
        self.explain.set("플레이어 x의 차례!")
        self.label = Label(frame1, textvariable=self.explain).pack(side=LEFT)
        Button(frame1, text="다시실행", command=self.refresh).pack(side=LEFT)

        window.mainloop()

MainGui()
