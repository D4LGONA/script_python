from tkinter import *
import random

def loadFile(path):
    f = open(path, 'r')
    data_list = f.read().split()
    f.close()
    return data_list

class MainGui:
    def judge


    def reset(self):
        s_word = random.choice(self.word_lists)
        answer = [[s_word[i], False] for i in range(len(s_word))]
        return answer

    def __init__(self):
        self.word_lists = loadFile("hangman.txt")
        self.answer = self.reset()

MainGui()
