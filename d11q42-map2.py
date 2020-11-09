my_list = []
for n in range(1,11):
    my_list.append(n)

even_num = list(map(lambda x:x**2, filter(lambda x:x%2==0, my_list)))

print(even_num)