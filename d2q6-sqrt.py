from math import sqrt

c = 50
h = 30
value = []
items = [x for x in input('input: ').split(',')]
for d in items:
    value.append(str(int(round(sqrt(2*c*float(d)/h)))))

print(','.join(value))