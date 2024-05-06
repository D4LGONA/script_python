# 14-4
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showerror

def show():
    try:
        f = open(filename.get())
        S = f.read()
        f.close()
        s = S.lower()
        histogram = [0] * 26
        for c in s:
            if c.isalpha():
                histogram[ord(c) - ord('a')] += 1
        for i in range(26):
            if histogram[i]:
                text.insert(END, chr(ord('a') + i) + " - " + str(histogram[i]) + '번 나타납니다.\n')
    except FileNotFoundError:
        showerror("에러", "파일을 찾을 수 없습니다.")

def openFile():
    filenameR = askopenfilename()
    filename.set(filenameR)

window = Tk()
window.title('문자 빈도수 세기')
frame1 = Frame(window)
frame1.pack()
scrollbar = Scrollbar(frame1)
scrollbar.pack(side=RIGHT, fill = Y)
text = Text(frame1, width=40, height=10, wrap=WORD, yscrollcommand=scrollbar.set)
text.pack()
scrollbar.config(command=text.yview)

frame2 = Frame(window)
frame2.pack()
Label(frame2, text='파일 입력:').pack(side=LEFT)
filename = StringVar()
Entry(frame2, width=20, textvariable=filename).pack(side=LEFT)
Button(frame2, text='열기', command=openFile).pack(side=LEFT)
Button(frame2, text='결과보기', command=show).pack(side=LEFT)

window.mainloop()
