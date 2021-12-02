text_file = 'H:\AdventOfCode\Day2.txt'

with open(text_file,'r') as f:
    lines = f.readlines()

horizontal = 0
depth = 0
aim = 0
instructions = []

for line in lines:
    instructions = line.split()
    
    if instructions[0] == 'forward':
        horizontal += int(instructions[1])
        depth += (aim*int(instructions[1]))
    elif instructions[0] == 'down':
        aim += int(instructions[1])
    else:
        aim -= int(instructions[1])

print(horizontal,depth,horizontal*depth)

