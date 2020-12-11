def num_generator(n):
    for i in range(0, n+1):
        if i%5==0 and i%7==0:
            yield i

n = int(input('Input n: '))
values = []
for i in num_generator(n):
    values.append(str(i))

print(','.join(values))