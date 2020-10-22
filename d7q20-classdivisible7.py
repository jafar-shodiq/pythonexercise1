class MyClass():
    def div_seven(seld, n):
        for i in range (0, int(n/7) + 1):
            yield i * 7

for i in MyClass().div_seven(int(input('input: '))):
    print(i)