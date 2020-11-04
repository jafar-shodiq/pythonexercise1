my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
my_list=[]

for n in my_tuple:
    if n%2 == 0:
        my_list.append(n)

my_tuple2 = tuple(my_list)
print(my_tuple2)
