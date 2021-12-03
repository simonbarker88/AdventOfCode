text_file = 'H:\AdventOfCode\Day3.txt'

with open(text_file,'r') as f:
    lines = f.readlines()

def most_frequent(List):
    return max(List, key = List.count)

def least_frequent(List):
    return min(List, key = List.count)

bits = []
most_frequent_bit = None
least_frequent_bit = None
gamma_rate = ''
epsilon_rate = ''
max_length = len(lines[0])
oxygen = []
c02 = []
temp_lines = []

for type in ['Oxygen','C02']:

    temp_lines = lines

    for i in range(max_length):
    
        bits = [x[i:i+1] for x in temp_lines]
        
        if type == 'Oxygen':
            bits.sort(reverse=True)
            most_frequent_bit = most_frequent(bits)
            gamma_rate += most_frequent_bit

            if len(oxygen) != 1:
                oxygen = [x for x in lines if x.startswith(gamma_rate)]

            temp_lines = oxygen
        else:
            bits.sort()
            least_frequent_bit = least_frequent(bits)
            epsilon_rate += least_frequent_bit
    
            if len(c02) != 1:
                c02 = [x for x in lines if x.startswith(epsilon_rate)]

            temp_lines = c02
   
print('Oxygen',int(oxygen[0],2),'\nc02',int(c02[0],2),'\nLife Support Rating',int(oxygen[0],2) * int(c02[0],2))


