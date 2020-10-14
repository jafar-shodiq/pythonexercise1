lines = []
while True:
    my_input = input()
    if my_input:
        lines.append(my_input.upper())
    else:
        break

for sentence in lines:
    print(sentence)