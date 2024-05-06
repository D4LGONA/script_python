from tkinter import *
import random

def loadFile(path):
    f = open(path, 'r')
    data_list = f.read().split()
    f.close()
    return data_list

class MainGui:
    def judge(self, answer, key):
        b = False
        for i in range(len(answer)):
            if key == answer[i][0]:
                answer[i][1] = True
                b = True
        return answer, b

    def toString(self, ans):
        result = ''
        if isinstance(ans[0], list):
            for i in range(len(ans)):
                if ans[i][1]:
                    result += ans[i][0]
                else:
                    result += '*'
        else:  # 일차원 배열인 경우
            for i in range(len(ans)):
                result += ans[i]
        return result

    def drawHangman(self):
        self.canvas.delete("hangman")
        self.canvas.create_arc(20, 200, 20+80, 200+40, start=0, extent=180)
        self.canvas.create_line(20+40, 200, 20+40, 20)
        self.canvas.create_line(20+40, 20, 20+40+100, 20)

        if len(self.miss) == 7: # 실패!
            for i in range(len(self.answer)):
                self.answer[i][1] = True
            self.canvas.create_text(200, 250, text='정답: ' + self.toString(self.answer),
                                    font='Times 14', tags='hangman')
            self.canvas.create_text(200, 270, text='계속하려면 Enter',
                                    font='Times 14', tags='hangman')
            self.isEnd = True
        elif self.isSuccess: # 성공!
            self.isEnd = True
            self.canvas.create_text(200, 250, text='정답: ' + self.toString(self.answer),
                                    font='Times 14', tags='hangman')
            self.canvas.create_text(200, 270, text='계속하려면 Enter',
                                    font='Times 14', tags='hangman')
        else:
            self.canvas.create_text(200, 250, text='단어 추측: ' + self.toString(self.answer),
                                    font='Times 14', tags='hangman')
            if len(self.miss) > 0:
                self.canvas.create_text(200, 270, text='틀린 글자: ' + self.toString(self.miss),
                                        font='Times 14', tags='hangman')

        if len(self.miss) < 1: return
        x1 = 20+40+100
        y1 = 20
        x2 = x1
        y2 = y1 + 20
        self.canvas.create_line(x1,y1,x2,y2,tags='hangman')

        if len(self.miss) < 2: return
        x3=x2
        y3=y2+20
        self.canvas.create_oval(x3-20,y3-20,x3+20,y3+20,tags='hangman')

        if len(self.miss) < 3: return
        self.canvas.create_line(x3,y3 + 20,x3-50,y3+70,tags='hangman')

        if len(self.miss) < 4: return
        self.canvas.create_line(x3,y3 + 20,x3+50,y3+70,tags='hangman')

        if len(self.miss) < 5: return
        x4=x3
        y4=y3+100
        self.canvas.create_line(x3,y3+20,x4,y4,tags='hangman')

        if len(self.miss) < 6: return
        self.canvas.create_line(x4,y4,x4-50,y4+50,tags='hangman')

        if len(self.miss) < 7: return
        self.canvas.create_line(x4,y4,x4+50,y4+50,tags='hangman')




    def reset(self):
        s_word = random.choice(self.word_lists)
        answer = [[s_word[i], False] for i in range(len(s_word))]
        return answer

    def keyEvent(self, Key):
        if Key.char.isalpha() and not self.isEnd:
            self.answer, b = self.judge(self.answer, Key.char)
            if not b: # 틀림!
                if Key.char not in self.miss:
                    self.miss.append(Key.char)

            self.isSuccess = True
            for i in self.answer:
                if not i[1]:
                    self.isSuccess = False
        elif Key.keycode == 13 and self.isEnd:
            self.answer = self.reset()
            self.miss = []
            self.isSuccess = False
            self.isEnd = False
        self.drawHangman()


    def __init__(self):
        window = Tk()
        window.title("hangman")
        self.canvas = Canvas(window, bg='white', width=400, height=300)
        self.canvas.pack()

        self.word_lists = loadFile("hangman.txt")
        self.answer = self.reset()
        self.miss = []
        self.isSuccess = False
        self.isEnd = False

        self.drawHangman()

        self.canvas.bind('<Key>', self.keyEvent)
        self.canvas.focus_set()

        window.mainloop()


MainGui()
