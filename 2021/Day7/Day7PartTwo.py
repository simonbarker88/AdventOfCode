text_file = 'H:\AdventOfCode\Day7.txt'

with open(text_file,'r') as f:
    lines = [int(x) for x in f.readlines()[0].split(',')]

min_fuel = None

for i in range(max(lines)):

    fuel = 0

    for crab in lines:
        dist = abs(i - crab)
        fuel += int(dist * (dist + 1) / 2)
    
    if not min_fuel or fuel < min_fuel:
        min_fuel = fuel 

print('Min Fuel Part B',min_fuel)