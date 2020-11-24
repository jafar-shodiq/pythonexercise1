import re

my_input = input('Enter your email: ')
pattern = r'(\w+)@(\w+)\.(com)'
answer = re.match(pattern, my_input)

print(answer.group(2))
