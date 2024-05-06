# 7-8
from time import *

class StopWatch:
    def __init__(self):
        self.__startTime = time()

    def start(self):
        self.__startTime = time()

    def stop(self):
        self.__endTime = time()

    def getElapsedTime(self):
        return int((self.__endTime - self.__startTime) * 1000)

sum = 0
s = StopWatch()
for i in range(1, 1000001):
    sum += i
s.stop()
print("실행시간: {0}".format(s.getElapsedTime()))
