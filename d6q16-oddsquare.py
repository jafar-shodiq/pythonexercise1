my_input = input('input: ')

my_list = [str(int(i)**2) for i in my_input.split(',') if int(i) % 2]
print(','.join(my_list))