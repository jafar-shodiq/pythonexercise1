class Shape():
    def __init__(self):
        pass
    
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        Shape.__init__(self)
        self.length = length
    
    def area(self):
        return self.length**2

square1 = Square(5)
print(square1.area())