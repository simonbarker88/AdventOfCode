text_file = 'H:\AdventOfCode\Day1Example.txt'

with open(text_file,'r') as f:
    lines = f.readlines()

count = 0
previous_value = 0
total_measurements = 0
current_value = 0

for line in lines:
    count += 1
    #print(f'line {count}: {line}') 
    current_value = int(line)

    if current_value > previous_value and count > 1:
        total_measurements += 1
    
    previous_value = current_value

print(total_measurements)
