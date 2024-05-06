SLOW = 1
MEDIUM = 2
FAST = 3

class Fan:
    def __init__(self, s = SLOW, r = 5, c = 'blue', o = False):
        self.__speed = s
        self.__on = o
        self.__radius = r
        self.__color = c

    def setSpeed(self, s):
        self.__speed = s
    def getSpeed(self):
        return self.__speed
    def setOn(self, o):
        self.__on = o
    def getOn(self):
        return self.__on
    def setRad(self, r):
        self.__radius = r
    def getRad(self):
        return self.__radius
    def setColor(self, c):
        self.__color = c
    def getColor(self):
        return self.__color

f1 = Fan(FAST, 10, 'yellow', True)
f2 = Fan(MEDIUM)
print('f1 - 속도 {0}, 반지름 {1}, 색상 {2}, 전원 {3}'.format(
    f1.getSpeed(), f1.getRad(), f1.getColor(), f1.getOn()))
print('f2 - 속도 {0}, 반지름 {1}, 색상 {2}, 전원 {3}'.format(
    f2.getSpeed(), f2.getRad(), f2.getColor(), f2.getOn()))
