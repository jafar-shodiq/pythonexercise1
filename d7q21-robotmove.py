import math

pos = [0,0]

while True:
    my_input= input()
    if not my_input:
        break
    movement = my_input.split(' ')
    direction = movement[0]
    steps = int(movement[1])
    
    if direction=='up':
        pos[0]+=steps
    elif direction=='down':
        pos[0]-=steps
    elif direction=='right':
        pos[1]+=steps
    elif direction=='left':
        pos[1]-=steps
    else:
        pass

print(int(round(math.sqrt(pos[1]**2+pos[0]**2))))