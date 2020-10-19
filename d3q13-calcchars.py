my_input = input('input: ')

my_dict = {"DIGITS":0, "LETTERS":0}

for char in my_input:
    if char.isdigit():
        my_dict["DIGITS"]+=1
    elif char.isalpha():
        my_dict["LETTERS"]+=1
    else:
        pass

print("LETTERS: ", my_dict["LETTERS"])
print("DIGITS: ", my_dict["DIGITS"])