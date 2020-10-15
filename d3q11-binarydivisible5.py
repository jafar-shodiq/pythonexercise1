my_input = input('input: ').split(',')
my_input = [num for num in my_input if int(num, 2) % 5 == 0]
print(','.join(my_input))