my_input = input('input: ')

my_dict = {"UPPER":0, "LOWER":0}

for char in my_input:
    if char.isupper():
        my_dict["UPPER"]+=1
    elif char.islower():
        my_dict["LOWER"]+=1
    else:
        pass

print("UPPER CASE: ", my_dict["UPPER"])
print("LOWER CASE: ", my_dict["LOWER"])