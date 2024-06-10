from tkinter import *
from tkinter import font

from winsound import PlaySound, SND_FILENAME

from card import Card
from player import Player
import random

class Game:
    def setupButton(self):
        button_width = 4
        button_height = 1
        button_spacing = 200

        # Player 1 betting buttons
        self.Bet5k_p1 = Button(self.window, text="5만", width=button_width, height=button_height, font=self.fontstyle, command=lambda: self.pressedBet(5, 0))
        self.Bet5k_p1.place(x=50, y=550)
        self.Bet1k_p1 = Button(self.window, text="1만", width=button_width, height=button_height, font=self.fontstyle, command=lambda: self.pressedBet(1, 0))
        self.Bet1k_p1.place(x=100, y=550)

        # Player 2 betting buttons
        self.Bet5k_p2 = Button(self.window, text="5만", width=button_width, height=button_height, font=self.fontstyle, command=lambda: self.pressedBet(5, 1))
        self.Bet5k_p2.place(x=50 + button_spacing, y=550)
        self.Bet1k_p2 = Button(self.window, text="1만", width=button_width, height=button_height, font=self.fontstyle, command=lambda: self.pressedBet(1, 1))
        self.Bet1k_p2.place(x=100 + button_spacing, y=550)

        # Player 3 betting buttons
        self.Bet5k_p3 = Button(self.window, text="5만", width=button_width, height=button_height, font=self.fontstyle, command=lambda: self.pressedBet(5, 2))
        self.Bet5k_p3.place(x=50 + 2 * button_spacing, y=550)
        self.Bet1k_p3 = Button(self.window, text="1만", width=button_width, height=button_height, font=self.fontstyle, command=lambda: self.pressedBet(1, 2))
        self.Bet1k_p3.place(x=100 + 2 * button_spacing, y=550)

        # Deal and Again buttons
        self.Deal = Button(self.window, text="Deal", width=button_width + 1, height=button_height, font=self.fontstyle, state=DISABLED, bg='gray', command=self.pressedDeal)
        self.Deal.place(x=650, y=550)
        self.Again = Button(self.window, text="Again", width=button_width + 1, height=button_height, font=self.fontstyle, state=DISABLED, bg='gray', command=self.pressedAgain)
        self.Again.place(x=720, y=550)

    def setupLabel(self):
        label_spacing = 200

        # Player 1 money label
        self.LplayerMoney_p1 = Label(text="0만", width=5, height=1, font=self.fontstyle, bg="green", fg="cyan")
        self.LplayerMoney_p1.place(x=75, y=500)

        # Player 2 money label
        self.LplayerMoney_p2 = Label(text="0만", width=5, height=1, font=self.fontstyle, bg="green", fg="cyan")
        self.LplayerMoney_p2.place(x=75 + label_spacing, y=500)

        # Player 3 money label
        self.LplayerMoney_p3 = Label(text="0만", width=5, height=1, font=self.fontstyle, bg="green", fg="cyan")
        self.LplayerMoney_p3.place(x=75 + 2 * label_spacing, y=500)

        # Shared money label
        self.LsharedMoney = Label(text="1000만", width=10, height=1, font=self.fontstyle, bg="green", fg="blue")
        self.LsharedMoney.place(x=650, y=250)

    def pressedBet(self, amount, player_idx):

        self.isbet[player_idx] = True
        # Update the player's money
        player_money_labels = [self.LplayerMoney_p1, self.LplayerMoney_p2, self.LplayerMoney_p3]
        shared_money = int(self.LsharedMoney.cget("text").replace("만", ""))

        if shared_money >= amount:
            PlaySound('sounds/chip.wav', SND_FILENAME)
            current_money = int(player_money_labels[player_idx].cget("text").replace("만", ""))
            new_money = current_money + amount
            player_money_labels[player_idx].configure(text=f"{new_money}만")

            # Update the shared money
            new_shared_money = shared_money - amount
            self.LsharedMoney.configure(text=f"{new_shared_money}만")

        if self.isbet == [True, True, True]:
            self.Deal['state'] = 'normal'
            self.Deal['bg'] = 'white'

    def pressedDeal(self):
        if len(self.players[0].cards) == 0:
            PlaySound('sounds/cardFlip1.wav', SND_FILENAME)
            self.isbet = [False, False, False]
            self.deal()
            self.Deal['state'] = 'disabled'
            self.Deal['bg'] = 'gray'
        elif len(self.players[0].cards) == 1:
            PlaySound('sounds/cardFlip1.wav', SND_FILENAME)
            self.isbet = [False, False, False]
            self.deal()
            self.deal()
            self.deal()
            self.Deal['state'] = 'disabled'
            self.Deal['bg'] = 'gray'
        else:
            self.deal()
            self.Deal['state'] = 'disabled'
            self.Deal['bg'] = 'gray'
            self.checkWinner()

    def pressedAgain(self):
        PlaySound('sounds/ding.wav', SND_FILENAME)
        if self.isWin == [False, False, False]:
            self.LplayerMoney_p1.configure(text="0만")
            self.LplayerMoney_p2.configure(text="0만")
            self.LplayerMoney_p3.configure(text="0만")
        if self.isWin[0] == True:
            adds = int(self.LplayerMoney_p1.cget("text").replace("만", ""))
            shared_money = int(self.LsharedMoney.cget("text").replace("만", ""))
            shared_money += adds * 2
            self.LsharedMoney.configure(text=f"{shared_money}만")
        if self.isWin[1] == True:
            adds = int(self.LplayerMoney_p2.cget("text").replace("만", ""))
            shared_money = int(self.LsharedMoney.cget("text").replace("만", ""))
            shared_money += adds * 2
            self.LsharedMoney.configure(text=f"{shared_money}만")
        if self.isWin[2] == True:
            adds = int(self.LplayerMoney_p3.cget("text").replace("만", ""))
            shared_money = int(self.LsharedMoney.cget("text").replace("만", ""))
            shared_money += adds * 2
            self.LsharedMoney.configure(text=f"{shared_money}만")
        self.LplayerMoney_p1.configure(text="0만")
        self.LplayerMoney_p2.configure(text="0만")
        self.LplayerMoney_p3.configure(text="0만")

        self.isbet = [False, False, False]
        self.isWin = [False, False, False]

        for label in self.LcardsPlayer:
            label.destroy()
        for label in self.LcardsDealer:
            label.destroy()
        for label in self.result_labels:  # 저장된 결과 라벨 삭제
            label.destroy()
        self.LcardsPlayer.clear()
        self.LcardsDealer.clear()
        self.result_labels.clear()

        self.Deal['state'] = 'disabled'
        self.Deal['bg'] = 'gray'
        self.Again['state'] = 'disabled'
        self.Again['bg'] = 'gray'

        self.players = [Player("player1"), Player("player2"), Player("player3")]
        self.dealer = Player("dealer")
        self.deck = [Card(i) for i in range(40)]
        random.shuffle(self.deck)

        self.Bet1k_p1['state'] = 'normal'
        self.Bet1k_p1['bg'] = 'white'
        self.Bet5k_p1['state'] = 'normal'
        self.Bet5k_p1['bg'] = 'white'
        self.Bet1k_p2['state'] = 'normal'
        self.Bet1k_p2['bg'] = 'white'
        self.Bet5k_p2['state'] = 'normal'
        self.Bet5k_p2['bg'] = 'white'
        self.Bet1k_p3['state'] = 'normal'
        self.Bet1k_p3['bg'] = 'white'
        self.Bet5k_p3['state'] = 'normal'
        self.Bet5k_p3['bg'] = 'white'

    def deal(self):
        positions = [(0, 350), (250, 350), (500, 350)]
        dealer_pos = [(250, 150), (300, 150), (350, 150), (400, 150), (450, 150)]

        for idx, player in enumerate(self.players):
            card = self.deck.pop()
            player.addCard(card)
            card_img = PhotoImage(file=card.filename())
            card_label = Label(self.window, image=card_img)
            card_label.image = card_img  # Keep a reference to avoid garbage collection
            card_label.place(x=positions[idx][0] + len(player.cards) * 40, y=positions[idx][1])
            self.LcardsPlayer.append(card_label)

            card_month_label = Label(self.window, text=str(card.month), font=self.fontstyle, bg="green", fg="white")
            card_month_label.place(x=positions[idx][0] + len(player.cards) * 40 + 15, y=positions[idx][1] - 30)
            self.LcardsPlayer.append(card_month_label)

        # Dealer's card should show the card back
        dealer_card = self.deck.pop()
        self.dealer.addCard(dealer_card)
        dealer_card_back_img = PhotoImage(file="GodoriCards/cardback.gif")  # Assuming the card back image is named "cardback.gif"
        dealer_card_label = Label(self.window, image=dealer_card_back_img)
        dealer_card_label.image = dealer_card_back_img  # Keep a reference to avoid garbage collection
        dealer_card_label.place(x=dealer_pos[len(self.dealer.cards) - 1][0], y=dealer_pos[len(self.dealer.cards) - 1][1])
        self.LcardsDealer.append(dealer_card_label)

    def checkWinner(self):
        self.Bet1k_p1['state'] = 'disabled'
        self.Bet1k_p1['bg'] = 'gray'
        self.Bet5k_p1['state'] = 'disabled'
        self.Bet5k_p1['bg'] = 'gray'
        self.Bet1k_p2['state'] = 'disabled'
        self.Bet1k_p2['bg'] = 'gray'
        self.Bet5k_p2['state'] = 'disabled'
        self.Bet5k_p2['bg'] = 'gray'
        self.Bet1k_p3['state'] = 'disabled'
        self.Bet1k_p3['bg'] = 'gray'
        self.Bet5k_p3['state'] = 'disabled'
        self.Bet5k_p3['bg'] = 'gray'

        # 뒤집힌 딜러 카드를 다시 그립니다.
        self.result_labels = []
        for i in range(5):
            p = PhotoImage(file=self.dealer.cards[i].filename())
            self.LcardsDealer[i].configure(image=p)
            self.LcardsDealer[i].image = p
            card_month_label = Label(self.window, text=str(self.dealer.cards[i].month), font=self.fontstyle, bg="green",
                                     fg="white")
            card_month_label.place(x=250 + i * 50 + 15, y=150 - 30)
            self.LcardsDealer.append(card_month_label)

        # 각 플레이어의 족보와 점수를 확인
        results = []
        for player in self.players:
            hand_name, hand_score, hand_name2, hand_score2 = player.check_hand()
            results.append((hand_name, hand_score, hand_name2, hand_score2))

        # 딜러의 족보와 점수를 확인
        dealer_hand_name, dealer_hand_score, dealer_hand_name2, dealer_hand_score2 = self.dealer.check_hand()

        for i in range(len(results)):
            if results[i][1] == 22:
                player_result_label = Label(self.window, text=results[i][0], font=self.fontstyle2, bg="green", fg="cyan")
            else:
                player_result_label = Label(self.window, text=results[i][0] + " " + results[i][2], font=self.fontstyle2,
                                            bg="green", fg="cyan")
            player_result_label.place(x=50 + i * 275, y=300)
            self.result_labels.append(player_result_label)

            if results[i][1] < dealer_hand_score or (results[i][1] <= dealer_hand_score and results[i][3] < dealer_hand_score2): # 이김
                self.isWin[i] = True
                result_text = "승"
                result_color = "red"
            else:
                result_text = "패"
                result_color = "blue"

            player_result = Label(self.window, text=result_text, font=self.fontstyle, bg="green", fg=result_color)
            player_result.place(x=0 + i * 275, y=300)
            self.result_labels.append(player_result)

        if dealer_hand_score == 22:
            dealer_result_label = Label(self.window, text=dealer_hand_name, font=self.fontstyle2, bg="green", fg="cyan")
        else:
            dealer_result_label = Label(self.window, text=dealer_hand_name + " " + dealer_hand_name2, font=self.fontstyle2,
                                        bg="green", fg="cyan")
        dealer_result_label.place(x=300, y=100)
        self.result_labels.append(dealer_result_label)

        if self.isWin == [False, False, False]:
            PlaySound('sounds/wrong.wav', SND_FILENAME)
        else:
            PlaySound('sounds/win.wav', SND_FILENAME)

        self.Again['state'] = 'normal'
        self.Again['bg'] = 'white'

    def __init__(self):
        self.window = Tk()
        self.window.title("도리짓고땡")
        self.window.geometry("800x600")
        self.window.configure(bg="green")
        self.fontstyle = font.Font(self.window, size=14, weight='bold', family='Consolas')
        self.fontstyle2 = font.Font(self.window, size=10, weight='bold', family='Consolas')
        self.setupButton()
        self.setupLabel()

        self.players = [Player("player1"), Player("player2"), Player("player3")]
        self.dealer = Player("dealer")
        self.deck = [Card(i) for i in range(40)]
        self.isbet = [False, False, False]
        random.shuffle(self.deck)
        self.LcardsPlayer = []
        self.LcardsDealer = []
        self.isWin = [False, False, False]
        self.result_labels = []

        self.window.mainloop()

Game()
