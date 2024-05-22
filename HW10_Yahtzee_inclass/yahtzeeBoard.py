from tkinter import *
from tkinter import font
import tkinter.messagebox
from player import *
from dice import *
from configuration import *

class YahtzeeBoard:
    UPPERTOTAL = 6
    UPPERBONUS = 7
    LOWERTOTAL = 15
    TOTAL = 16
    dice = []
    diceButtons = []
    fields = []
    players = []
    numPlayers = 0
    player = 0
    round = 0
    roll = 0

    def __init__(self):
        self.InitPlayers()

    def InitPlayers(self):
        self.pwindow = Tk()
        self.TempFont = font.Font(size=16, weight='bold', family='Consolas')
        self.label = []
        self.entry = []
        self.label.append(Label(self.pwindow, text='플레이어 명수', font=self.TempFont))
        self.label[0].grid(row=0, column=0)
        for i in range(1, 11): # 10개?
            self.label.append(Label(self.pwindow, text='플레이어'+str(i)+'이름', font=self.TempFont))
            self.label[i].grid(row=i, column=0)
        for i in range(11): # 11개/?
            self.entry.append(Entry(self.pwindow, text='플레이어' + str(i) + '이름', font=self.TempFont))
            self.entry[i].grid(row=i, column=1)
        Button(self.pwindow, text='Yahtzee 플레이어 설정 완료', font=self.TempFont, command=self.playerName).grid(row=11, column=0)
        self.pwindow.mainloop()

    def playerName(self):
        self.numPlayers = int(self.entry[0].get())
        for i in range(1, self.numPlayers+1):
            self.players.append(Player(str(self.entry[i].get())))
        self.pwindow.destroy()
        self.initInterface()

    def initInterface(self):
        self.window = Tk('Yahtzee Game')
        self.window.geometry('1024x800')
        self.TempFont = font.Font(size=12, weight='bold', family='Consolas')
        for i in range(5):
            self.dice.append(Dice())
        self.rollDice = Button(self.window, text='Roll Dice', font=self.TempFont, command=self.rollDiceListener)
        self.rollDice.grid(row=0, column=0)
        for i in range(5):
            self.diceButtons.append(Button(self.window, text='?', font=self.TempFont, width=8,
                                           command=lambda row=i:self.diceListener(row)))
            self.diceButtons[i].grid(row=i+1, column=0)

        for i in range(self.TOTAL + 2): #18행
            Label(self.window, text=Configuration.configs[i], font=self.TempFont).grid(row=i, column=1)
            for j in range(self.numPlayers):
                if i == 0:
                    Label(self.window, text=self.players[j].name, font=self.TempFont).grid(row=i, column=2+j)
                else:
                    if j == 0:
                        self.fields.append(list())
                        # i-1행에 플레이어 개수 만큼 버튼 추가하고 이벤트 Listener 설정, 매개변수 설정
                        self.fields[i - 1].append(Button(self.window, text="", font=self.TempFont, width=8,
                                                         command=lambda row=i - 1: self.categoryListener(row)))
                        self.fields[i - 1][j].grid(row=i, column=2 + j)
                        # 누를 필요없는 버튼은 disable 시킴
                        if (j != self.player or (i - 1) == self.UPPERTOTAL or (i - 1) == self.UPPERBONUS
                                or (i - 1) == self.LOWERTOTAL or (i - 1) == self.TOTAL):
                            self.fields[i - 1][j]['state'] = 'disabled'
                            self.fields[i - 1][j]['bg'] = 'light gray'

        self.bottomLabel = Label(self.window, text=self.players[self.player].toString() +
                                                   "차례: Roll Dice 버튼을 누르세요", width=35, font=self.TempFont)
        self.bottomLabel.grid(row=self.TOTAL + 2, column=0)
        self.window.mainloop()

    def categoryListener(self):
        pass

    def rollDiceListener(self):
        pass

    def diceListener(self, row):
        self.diceButtons[row]['state']='diabled'
        self.diceButtons[row]['bg']='light gray'


YahtzeeBoard()