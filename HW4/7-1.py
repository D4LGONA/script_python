# 7-1

class Rectangle:
    def __init__(self, w=1, h=2):
        self.width = w
        self.height = h
        
    def getArea(self):
        return self.width * self.height
    
    def getPerimeter(self):
        return 2 * (self.width + self.height)
    
r1 = Rectangle(4, 10)
r2 = Rectangle(3.5, 35.7)

print("r1: 폭 {0}, 높이 {1}, 넓이 {2}, 둘레 {3}".format(
    r1.width, r1.height, r1.getArea(), r1.getPerimeter()))
print("r2: 폭 {0}, 높이 {1}, 넓이 {2}, 둘레 {3}".format(
    r2.width, r2.height, r2.getArea(), r2.getPerimeter()))
