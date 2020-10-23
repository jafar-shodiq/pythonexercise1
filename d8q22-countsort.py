my_input = input('input: ').split(' ')

word = sorted(set(my_input))

for i in word:
    print(f'{i}: {my_input.count(i)}')