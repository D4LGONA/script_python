# 14-7
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

        width = int(canvas['width'])
        height = int(canvas['height'])
        maxCounts = max(histogram)
        heightBar = height * 0.75
        widthBar = width - 20
        for i in range(26):
            canvas.create_rectangle(10 + i * widthBar / 26,
                                    height - 20,
                                    10 + (i + 1) * widthBar / 26,
                                    height - heightBar * histogram[i] / maxCounts - 20)
            canvas.create_text(i*widthBar/26 + 10 + 0.5 * widthBar/26, height - 10, text = chr(i+ord('a')))
            #canvas.create_text(10+i*)


    except FileNotFoundError:
        showerror("에러", "파일을 찾을 수 없습니다.")

def openFile():
    filenameR = askopenfilename()
    filename.set(filenameR)

window = Tk()
window.title('문자 빈도수 세기')
frame1 = Frame(window)
frame1.pack()
canvas = Canvas(frame1, width=500, height=200)
canvas.pack()

frame2 = Frame(window)
frame2.pack()
Label(frame2, text='파일 입력:').pack(side=LEFT)
filename = StringVar()
Entry(frame2, width=20, textvariable=filename).pack(side=LEFT)
Button(frame2, text='열기', command=openFile).pack(side=LEFT)
Button(frame2, text='결과보기', command=show).pack(side=LEFT)

window.mainloop()
