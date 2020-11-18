def fn(num):
    return num/0

try:
    print(fn(5))
except ZeroDivisionError:
    raise