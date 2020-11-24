import re

my_input = input('Input: ')
pattern = r'\d'
answer = re.findall(pattern, my_input)
print(answer)