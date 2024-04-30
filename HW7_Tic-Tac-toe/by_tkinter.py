from tkinter import *

class MainGui:
    def check(self):
        for i in range(3):
            if self.matrix[0][i]['text'] == self.matrix[1][i]['text'] == self.matrix[2][i]['text'] != " ":
                return True
            if self.matrix[i][0]['text'] == self.matrix[i][1]['text'] == self.matrix[i][2]['text'] != " ":
                return True
        if self.matrix[0][0]['text'] == self.matrix[1][1]['text'] == self.matrix[2][2]['text'] != " ":
            return True
        if self.matrix[2][0]['text'] == self.matrix[1][1]['text'] == self.matrix[0][2]['text'] != " ":
            return True

        return False

    def pressed(self, row, col):
        if not self.done and self.matrix[row][col]['text'] == ' ':
            if self.turn:
                self.matrix[row][col]['image'] = self.imageX
                self.matrix[row][col]['text'] = 'x'
            else:
                self.matrix[row][col]['image'] = self.imageO
                self.matrix[row][col]['text'] = 'o'
            self.cnt += 1
            if self.check():
                self.done = True
                if self.turn:
                    self.explain.set("플레이어 x가 이겼습니다!")
                else:
                    self.explain.set("플레이어 o가 이겼습니다!")
                self.cnt = 0
                return
            else:
                if self.cnt == 9:
                    self.explain.set("비겼습니다.")
                    self.cnt = 0
                    return

            self.turn = not self.turn
            if self.turn:
                self.explain.set("플레이어 x의 차례!")
            else:
                self.explain.set("플레이어 o의 차례!")

    def refresh(self):
        for i in range(3):
            for j in range(3):
                self.matrix[i][j]['image'] = self.imageE
                self.matrix[i][j]['text'] = " "
        self.done = False
        self.explain.set("플레이어 x의 차례!")
        self.turn = True

    def __init__(self):
        window = Tk()
        window.title('Tic-Tac-Toe')
        frame = Frame(window)
        frame.pack()
        self.matrix = []
        self.imageX = PhotoImage(file='resources/x.gif')
        self.imageO = PhotoImage(file='resources/o.gif')
        self.imageE = PhotoImage(file='resources/empty.gif')
        self.turn = True
        self.done = False
        self.cnt = 0
        for i in range(3):
            self.matrix.append([])
            for j in range(3):
                btn = Button(frame, image=self.imageE, text=' ',
                             command=lambda row=i, col=j: self.pressed(row, col),
                             bd=0, highlightthickness=0)
                btn.grid(row=i, column=j)
                self.matrix[i].append(btn)

        frame1 = Frame(window)
        frame1.pack()
        self.explain = StringVar()
        self.explain.set("플레이어 x의 차례!")
        self.label = Label(frame1, textvariable=self.explain)
        self.label.pack()
        Button(frame1, text="다시실행", command=self.refresh).pack()

        window.mainloop()

MainGui()
