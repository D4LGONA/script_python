class Card:
    def __init__(self, temp):
        self.value = temp % 4 + 1
        self.month = temp // 4 + 1

    def filename(self):
        path = "GodoriCards/" + str(self.month)+"."+str(self.value)+".gif"
        print(path)
        return path