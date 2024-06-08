from tkinter import *
from tkinter import font
from winsound import *
from card import *
from player import *
import random


class BlackJack:
    def setupButton(self):
        self.Check = Button(self.window, text="Check", width=6, height=1, font=self.fontstyle2, command=self.pressedCheck)
        self.Check.place(x=50, y=500)
        self.Bx1 = Button(self.window, text="Bet x1", width=6, height=1, font=self.fontstyle2, command=self.pressedBx1)
        self.Bx1.place(x=150, y=500)
        self.Bx2 = Button(self.window, text="Bet x2", width=6, height=1, font=self.fontstyle2, command=self.pressedBx2)
        self.Bx2.place(x=250, y=500)
        self.Deal = Button(self.window, text="Deal", width=6, height=1, font=self.fontstyle2, command=self.pressedDeal)
        self.Deal.place(x=600, y=500)
        self.Again = Button(self.window, text="Again", width=6, height=1, font=self.fontstyle2, command=self.pressedAgain)
        self.Again.place(x=700, y=500)

        self.Deal['state'] = 'disabled'
        self.Deal['bg'] = 'gray'
        self.Again['state'] = 'disabled'
        self.Again['bg'] = 'gray'

    def setupLabel(self):
        self.LbetMoney = Label(text="$10", width=4, height=1, font=self.fontstyle, bg="green", fg="cyan")
        self.LbetMoney.place(x=200, y=450)
        self.LplayerMoney = Label(text="You have $1000", width=15, height=1, font=self.fontstyle, bg="green", fg="cyan")
        self.LplayerMoney.place(x=500, y=450)

        self.LplayerPts = Label(text="", width=15, height=1, font=self.fontstyle2, bg="green", fg="white")
        self.LplayerPts.place(x=300, y=350)
        self.LdealerPts = Label(text="", width=15, height=1, font=self.fontstyle2, bg="green", fg="white")
        self.LdealerPts.place(x=300, y=100)

        self.winner = Label(text="", width=15, height=1, font=self.fontstyle, bg="green", fg="white")
        self.winner.place(x=500, y=300)



    def pressedBx1(self):
        if self.nCardsPlayer == 0: # 아직 시작되지 않음
            self.betMoney *= 2
            self.playerMoney -= self.betMoney
            self.LplayerMoney.configure(text="You have $" + str(self.playerMoney))
            self.Deal["state"] = "active"
            self.Deal["bg"] = "white"
            PlaySound('resource/sounds/chip.wav', SND_FILENAME)
            self.LbetMoney.configure(text="$" + str(self.betMoney))

            # deal만 active
            self.Bx1['state'] = 'disabled'
            self.Bx1['bg'] = 'gray'
            self.Bx2['state'] = 'disabled'
            self.Bx2['bg'] = 'gray'
            self.Deal['state'] = 'active'
            self.Deal['bg'] = 'white'
            self.Again['state'] = 'disabled'
            self.Again['bg'] = 'gray'
            self.Check['state'] = 'disabled'
            self.Check['bg'] = 'gray'
            if self.nCardsBoard == 5:
                self.checkWinner()

        # bx1을 누르면 지금 배팅된 금액만큼 더냄
        elif self.betMoney <= self.playerMoney: # 낼 돈이 되면 - deal만 활성화.
            self.playerMoney -= self.betMoney
            self.LplayerMoney.configure(text="You have $" + str(self.playerMoney))
            self.Deal["state"] = "active"
            self.Deal["bg"] = "white"
            PlaySound('resource/sounds/chip.wav', SND_FILENAME)
            self.betMoney *= 2
            self.LbetMoney.configure(text="$" + str(self.betMoney))

            # deal만 active
            self.Bx1['state'] = 'disabled'
            self.Bx1['bg'] = 'gray'
            self.Bx2['state'] = 'disabled'
            self.Bx2['bg'] = 'gray'
            self.Deal['state'] = 'active'
            self.Deal['bg'] = 'white'
            self.Again['state'] = 'disabled'
            self.Again['bg'] = 'gray'
            self.Check['state'] = 'disabled'
            self.Check['bg'] = 'gray'
            if self.nCardsBoard == 5:
                self.checkWinner()


    def pressedBx2(self):
        if self.nCardsPlayer == 0:  # 아직 시작되지 않음
            self.betMoney += self.betMoney * 2
            self.playerMoney -=  self.betMoney
            self.LplayerMoney.configure(text="You have $" + str(self.playerMoney))
            self.Deal["state"] = "active"
            self.Deal["bg"] = "white"
            PlaySound('resource/sounds/chip.wav', SND_FILENAME)
            self.LbetMoney.configure(text="$" + str(self.betMoney))

            # deal만 active
            self.Check['state'] = 'disabled'
            self.Check['bg'] = 'gray'
            self.Bx1['state'] = 'disabled'
            self.Bx1['bg'] = 'gray'
            self.Bx2['state'] = 'disabled'
            self.Bx2['bg'] = 'gray'
            self.Deal['state'] = 'active'
            self.Deal['bg'] = 'white'
            self.Again['state'] = 'disabled'
            self.Again['bg'] = 'gray'
            if self.nCardsBoard == 5:
                self.checkWinner()

        # bx2을 누르면 지금 배팅된 금액의 2배를 더냄
        elif (self.betMoney * 2) <= self.playerMoney:
            self.playerMoney -= self.betMoney * 2
            self.LplayerMoney.configure(text="You have $" + str(self.playerMoney))
            self.Deal["state"] = "active"
            self.Deal["bg"] = "white"
            PlaySound('resource/sounds/chip.wav', SND_FILENAME)
            self.betMoney += self.betMoney * 2
            self.LbetMoney.configure(text="$" + str(self.betMoney))

            # deal만 active
            self.Check['state'] = 'disabled'
            self.Check['bg'] = 'gray'
            self.Bx1['state'] = 'disabled'
            self.Bx1['bg'] = 'gray'
            self.Bx2['state'] = 'disabled'
            self.Bx2['bg'] = 'gray'
            self.Deal['state'] = 'active'
            self.Deal['bg'] = 'white'
            self.Again['state'] = 'disabled'
            self.Again['bg'] = 'gray'
            if self.nCardsBoard == 5:
                self.checkWinner()

    def pressedDeal(self):
        self.deal()
        self.Deal['state'] = 'disabled'
        self.Deal['bg'] = 'gray'
        self.Again['state'] = 'disabled'
        self.Again['bg'] = 'gray'

    def pressedAgain(self):
        self.LbetMoney.configure(text="$10")
        self.LplayerPts.configure(text="")
        self.LdealerPts.configure(text="")

        for label in self.LcardsPlayer:
            label.destroy()
        for label in self.LcardsDealer:
            label.destroy()
        for label in self.LcardsBoard:
            label.destroy()
        self.LcardsDealer.clear()
        self.LcardsPlayer.clear()
        self.LcardsBoard.clear()

        self.betMoney = 10
        self.nCardsDealer = 0
        self.nCardsBoard = 0
        self.nCardsPlayer = 0
        self.deckN = 0
        self.winner.configure(text="")

        self.setupButton()


    def compare_players(self, player1, player2):
        rank1, hand_type1, hand_values1 = player1.checking()
        rank2, hand_type2, hand_values2 = player2.checking()

        if rank1 > rank2:
            winner = player1
        elif rank2 > rank1:
            winner = player2
        else:
            if hand_values1[0].value > hand_values2[0].value:
                winner = player1
            elif hand_values2[0].value > hand_values1[0].value:
                winner = player2
            else:
                winner = None

        return winner, rank1, hand_type1, rank2, hand_type2


    def checkWinner(self):
        # 뒤집힌 카드를 다시 그린다.
        p = PhotoImage(file="resource/cards/" + self.dealer.cards[0].filename())
        self.LcardsDealer[0].configure(image=p)  # 이미지 레퍼런스 변경
        self.LcardsDealer[0].image = p  # 파이썬은 라벨 이미지 레퍼런스를 갖고 있어야 이미지가 보임
        p = PhotoImage(file="resource/cards/" + self.dealer.cards[1].filename())
        self.LcardsDealer[1].configure(image=p)  # 이미지 레퍼런스 변경
        self.LcardsDealer[1].image = p  # 파이썬은 라벨 이미지 레퍼런스를 갖고 있어야 이미지가 보임

        winner, rank1, hand_type1, rank2, hand_type2 = self.compare_players(self.player, self.dealer)


        if winner == self.player:
            self.playerMoney += self.betMoney * 2
            PlaySound('resource/sounds/win.wav', SND_FILENAME)
            self.winner.configure(text="win!")
        elif winner == self.dealer:
            PlaySound('resource/sounds/wrong.wav', SND_FILENAME)
            self.winner.configure(text="lost!")
        else:
            self.playerMoney += self.betMoney
            PlaySound('resource/sounds/ding.wav', SND_FILENAME)
            self.winner.configure(text="tie!")

        self.LplayerPts.configure(text=hand_type1)
        self.LdealerPts.configure(text=hand_type2)

        self.betMoney = 0
        self.LplayerMoney.configure(text="You have $" + str(self.playerMoney))
        self.LbetMoney.configure(text="$" + str(self.betMoney))
        self.Deal['state'] = 'disabled'
        self.Deal['bg'] = 'gray'
        self.Again['state'] = 'active'
        self.Again['bg'] = 'white'

    def pressedCheck(self):
        if self.nCardsPlayer == 0:
            self.playerMoney -= self.betMoney
            self.LplayerMoney.configure(text="You have $" + str(self.playerMoney))
            PlaySound('resource/sounds/chip.wav', SND_FILENAME)
            self.LbetMoney.configure(text="$" + str(self.betMoney))


        self.Bx1['state'] = 'disabled'
        self.Bx1['bg'] = 'gray'
        self.Bx2['state'] = 'disabled'
        self.Bx2['bg'] = 'gray'
        self.Deal['state'] = 'active'
        self.Deal['bg'] = 'white'
        self.Again['state'] = 'disabled'
        self.Again['bg'] = 'gray'
        self.Check['state'] = 'disabled'
        self.Check['bg'] = 'gray'
        if self.nCardsBoard == 5:
            self.checkWinner()


    def boardDeal(self):
        newCard = Card(self.cardDeck[self.deckN])

        self.deckN += 1
        self.player.addCard(newCard)
        self.dealer.addCard(newCard)
        p = PhotoImage(file=newCard.filename())
        self.LcardsBoard.append(Label(self.window, image=p))
        self.LcardsBoard[self.nCardsBoard].image = p
        self.LcardsBoard[self.nCardsBoard].place(x=250 + self.nCardsBoard * 100, y=200)
        self.nCardsBoard += 1


    def playerDeal(self): # 플레이어에게 카드깔기
        newCard = Card(self.cardDeck[self.deckN])

        self.deckN += 1
        self.player.addCard(newCard)
        p = PhotoImage(file=newCard.filename())
        self.LcardsPlayer.append(Label(self.window, image=p))
        self.LcardsPlayer[self.player.inHand() - 1].image = p
        self.LcardsPlayer[self.player.inHand() - 1].place(x=50 + self.nCardsPlayer * 100, y=320)
        self.nCardsPlayer += 1

    def dealerDeal(self): # 딜러한테 카드깔기
        newCard = Card(self.cardDeck[self.deckN])

        self.deckN += 1
        self.dealer.addCard(newCard)
        p = PhotoImage(file="resource/cards/b2fv.png")
        self.LcardsDealer.append(Label(self.window, image=p))
        self.LcardsDealer[self.dealer.inHand() - 1].image = p
        self.LcardsDealer[self.dealer.inHand() - 1].place(x=50 + self.nCardsDealer * 100, y=80)
        self.nCardsDealer += 1


    def deal(self):
        PlaySound('resource/sounds/cardFlip1.wav', SND_FILENAME)

        if self.nCardsPlayer == 0:
            self.player.reset()
            self.dealer.reset()  # 카드 덱 52장 셔플링 0,1,,.51
            self.cardDeck = [i for i in range(52)]
            random.shuffle(self.cardDeck)
            self.deckN = 0

            self.playerDeal()
            self.dealerDeal()
            self.playerDeal()
            self.dealerDeal()

        else:
            if self.nCardsBoard == 0:
                self.boardDeal()
                self.boardDeal()
                self.boardDeal()
            else:
                self.boardDeal()

        self.Check['state'] = 'active'
        self.Check['bg'] = 'white'
        self.Bx1['state'] = 'active'
        self.Bx1['bg'] = 'white'
        self.Bx2['state'] = 'active'
        self.Bx2['bg'] = 'white'



    def __init__(self):
        self.window = Tk()
        self.window.title("도리짓고땡")
        self.window.geometry("800x600")
        self.window.configure(bg="green")
        self.fontstyle = font.Font(self.window, size=24, weight='bold', family='Consolas')
        self.fontstyle2 = font.Font(self.window, size=16, weight='bold', family='Consolas')
        self.setupButton()
        self.setupLabel()

        self.player = Player("player")
        self.dealer = Player("dealer")
        self.betMoney = 10
        self.playerMoney = 1000
        self.nCardsDealer = 0
        self.nCardsPlayer = 0ㄴ
        self.nCardsBoard = 0
        self.LcardsPlayer = []
        self.LcardsDealer = []
        self.LcardsBoard = []
        self.deckN = 0

        self.window.mainloop()

BlackJack()
