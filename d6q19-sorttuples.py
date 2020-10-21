my_list = []
while True:
    my_input = input('input: ').split(',')
    if not my_input[0]:
        break
    my_list.append(tuple(my_input))

my_list.sort(key=lambda x:(x[0], int(x[1]), int(x[2])))
print(my_list)