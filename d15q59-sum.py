n = int(input('Input n: '))
sum = 0

for i in range (1, n+1):
    sum += i/(i+1)

print(f'{sum:.2f}')