class ModifyString:
    def __init__(self):
        self.input = ''
    
    def getString(self):
        self.input = input('input: ')

    def printString(self):
        print(self.input.upper())

obj1 = ModifyString()
obj1.getString()
obj1.printString()