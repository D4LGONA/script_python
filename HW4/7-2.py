# 7-2

class Stock:
    def __init__(self, s, n, p, c):
        self.__symbol = s
        self.__name = n
        self.__previousClosingPrice = p
        self.__currentPrice = c

    def getName(self):
        return self.__name
    
    def getSymbol(self):
        return self.__symbol
    
    def getCP(self):
        return self.__currentPrice
    
    def getPCP(self):
        return self.__previousClosingPrice
    
    def setCP(self, cp):
        self.__currentPrice = cp
        
    def getPCP(self, pcp):
        self.__previousClosingPrice = pcp
        
    def getChangePercent(self):
        n = (self.__currentPrice - self.__previousClosingPrice)
        return 100 * n / self.__previousClosingPrice

s = Stock("INTC", "Intel Corporation", 20500, 20350)
print("{0}의 가격변동률: {1:.2f}".format(s.getName(), s.getChangePercent()) )
