text_file = 'H:\AdventOfCode\Day1.txt'

with open(text_file,'r') as f:
    lines = f.readlines()

count = 0
previous_value = 0
total_measurements = 0
current_value = 0
window = []

for line in lines:
    count += 1

    window.append(int(line))
    
    if count >= 3:
            
        current_value = sum(window)

        if current_value > previous_value and previous_value != 0:
            total_measurements += 1
    
        previous_value = current_value
        window.pop(0)

print(total_measurements)

