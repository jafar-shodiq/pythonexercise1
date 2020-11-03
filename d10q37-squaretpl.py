def fn():
    my_list=[]
    for i in range(1, 21):
        my_list.append(i**2)
    
    print(tuple(my_list))

fn()