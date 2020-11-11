class Circle():
    def __init__(self, rad):
        self.rad = rad
    
    def area(self): # phi*(rad**2)
        return 3.14*(self.rad**2)

area1 = Circle(5)
print(area1.area())
