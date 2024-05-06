# 9-2
from tkinter import *

def cal():
    p = float(money.get()) * (1 + (float(AIR.get())/1200)) ** (float(period.get())*12)
    PV.set(p)

window = Tk()
window.title("투자금 계산")
Label(window, text='투자금').grid(row=1, column=1, sticky=W)
Label(window, text='기간').grid(row=2, column=1, sticky=W)
Label(window, text='연이율').grid(row=3, column=1, sticky=W)
Label(window, text='미래 가치').grid(row=4, column=1, sticky=W)
money = StringVar()
Entry(window, textvariable=money, justify=RIGHT).grid(row=1, column=2)
period = StringVar()
Entry(window, textvariable=period, justify=RIGHT).grid(row=2, column=2)
AIR = StringVar()
Entry(window, textvariable=AIR, justify=RIGHT).grid(row=3, column=2)
PV = StringVar()
Label(window, textvariable=PV).grid(row=4, column=2, sticky=E)
Button(window, text='계산하기', command=cal).grid(row=5, column=2, sticky=E)

window.mainloop()
