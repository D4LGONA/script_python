# 12-1
class GeometricObject:
    def __init__(self, color, isFill):
        self.color = color
        self.filled = isFill

class Triangle(GeometricObject):
    def __init__(self, c, isF, s1=1.0, s2=1.0, s3=1.0):
        f = False
        if isF == 1:
            f = True
        super().__init__(c, f)
        self.side1 = s1
        self.side2 = s2
        self.side3 = s3

    def setS1(self, v):
        self.side1 = v
    def setS2(self, v):
        self.side2 = v
    def setS3(self, v):
        self.side3 = v

    def getArea(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        return(s * (s-self.side1)*(s-self.side2)*(s-self.side3))**0.5
    def getPerimeter(self):
        return self.side1+self.side2+self.side3
    def __str__(self):
        return("Triangle: side1 = " + str(self.side1) +
               ", side2 = " + str(self.side2) +
               ", side3 = " + str(self.side3) +
               ", color = " + str(self.color) +
               ", isFilled = " + str(self.filled) +
               ", Area = " + str(self.getArea()) +
               ", Perimeter = " + str(self.getPerimeter()))

t = Triangle('yellow', 1, 2.0, 2.0, 2.0)
print(t.__str__())