def fn():
    my_list = []
    for i in range(1, 21):
        my_list.append(i**2)
    print(my_list[-5:])

fn()