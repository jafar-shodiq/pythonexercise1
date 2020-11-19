class CustomException(Exception):
    '''
    There is an error!!!
    '''
    pass
    
    def __init__(self, message):
        self.message = message
        pass

my_error = CustomException('There is an error in your code, dunno what it is though')
print(my_error)