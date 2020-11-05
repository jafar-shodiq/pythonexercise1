my_list = []
for i in range(1,11):
    my_list.append(i)

squared = list(map(lambda x:x**2, my_list))
print(squared)