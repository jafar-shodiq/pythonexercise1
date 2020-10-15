my_input = input('input: ').split()

for i in my_input:
    if my_input.count(i) > 1:
        my_input.remove(i)

my_input.sort()
print(" ".join(my_input))