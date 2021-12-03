text_file = 'H:\AdventOfCode\Day3.txt'

with open(text_file,'r') as f:
    lines = f.readlines()

def most_frequent(List):
    return max(set(List), key = List.count)

def least_frequent(List):
    return min(set(List), key = List.count)

bits = []
most_frequent_bit = None
least_frequent_bit = None
gamma_rate = ''
epsilon_rate = ''
max_length = len(lines[0])

for i in range(max_length):
    
    bits = [x[i:i+1] for x in lines]

    most_frequent_bit = most_frequent(bits)
    least_frequent_bit = least_frequent(bits)

    gamma_rate += most_frequent_bit
    epsilon_rate += least_frequent_bit
   
print('Gamma Rate',int(gamma_rate,2),'\nEpsilon Rate',int(epsilon_rate,2),'\nPower',int(epsilon_rate,2) * int(gamma_rate,2))

