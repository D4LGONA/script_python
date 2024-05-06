from tkinter import *

class MainGui:
    def check_win(self):
        for i in range(6):  # 가로
            for j in range(4):
                player = self.matrix[i][j]['text']
                if player != ' ' and player == self.matrix[i][j + 1]['text'] and player == self.matrix[i][j + 2]['text'] \
                        and player == self.matrix[i][j + 3]['text']:
                    return True

        for i in range(3):  # 세로
            for j in range(7):
                player = self.matrix[i][j]['text']
                if player != ' ' and player == self.matrix[i + 1][j]['text'] and player == self.matrix[i + 2][j]['text'] \
                        and player == self.matrix[i + 3][j]['text']:
                    return True

        for i in range(3):
            for j in range(4):
                player = self.matrix[i][j]['text']
                if player != ' ' and player == self.matrix[i + 1][j + 1]['text'] and player == self.matrix[i + 2][j + 2]['text'] \
                        and player == self.matrix[i + 3][j + 3]['text']:
                    return True

        for i in range(3):
            for j in range(3, 7):
                player = self.matrix[i][j]['text']
                if player != ' ' and player == self.matrix[i + 1][j - 1]['text'] and player == self.matrix[i + 2][j - 2]['text']\
                        and player == self.matrix[i + 3][j - 3]['text']:
                    return True

        return False

    def findRow(self, col):
        for row in range(5,-1,-1):
            if self.matrix[row][col]['text'] == ' ':
                return row
        return 6

    def pressed(self, col):
        row = self.findRow(col)
        if row == 6: return
        if not self.done and self.matrix[row][col]['text'] == ' ':
            if self.turn:
                self.matrix[row][col]['image'] = self.imageX
                self.matrix[row][col]['text'] = 'x'
            else:
                self.matrix[row][col]['image'] = self.imageO
                self.matrix[row][col]['text'] = 'o'
            self.cnt += 1
            if self.check_win():
                self.done = True
                if self.turn:
                    self.explain.set("플레이어 x가 이겼습니다!")
                else:
                    self.explain.set("플레이어 o가 이겼습니다!")
                self.cnt = 0
                return
            else:
                if self.cnt == 42:
                    self.explain.set("비겼습니다.")
                    self.cnt = 0
                    return

            self.turn = not self.turn
            if self.turn:
                self.explain.set("플레이어 x의 차례!")
            else:
                self.explain.set("플레이어 o의 차례!")

    def refresh(self):
        for i in range(6):
            for j in range(7):
                self.matrix[i][j]['image'] = self.imageE
                self.matrix[i][j]['text'] = " "
        self.done = False
        self.explain.set("플레이어 x의 차례!")
        self.turn = True

    def __init__(self):
        window = Tk()
        window.title('사목게임')
        frame = Frame(window)
        frame.pack()
        self.matrix = []
        self.imageX = PhotoImage(file='resources/x.gif')
        self.imageO = PhotoImage(file='resources/o.gif')
        self.imageE = PhotoImage(file='resources/empty.gif')
        self.turn = True
        self.done = False
        self.cnt = 0
        for i in range(6):
            self.matrix.append([])
            for j in range(7):
                btn = Button(frame, image=self.imageE, text=' ',
                             command=lambda col=j: self.pressed(col),
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
