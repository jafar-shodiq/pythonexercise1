import re

my_input = input('input: ').split(',')

'''
At least 1 letter between [a-z]
At least 1 number between [0-9]
At least 1 letter between [A-Z]
At least 1 character from [$#@]
Minimum length of transaction password: 6
Maximum length of transaction password: 12
'''

pattern = re.compile(r"^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[$#@]).{6,12}$")

for i in my_input:
    if pattern.fullmatch(i):
        print(i)
    else:
        print('check the requirements')