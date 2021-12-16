from functools import reduce
from collections import Counter

text_file = 'H:\AdventOfCode\Day9.txt'

with open(text_file,'r') as f:
        area = [[int(char) for char in x if char != "\n"] for x in f.readlines()]

def calc_basin(y, x):
    adjacent = [(y-1, x), (y+1, x), (y, x-1), (y, x+1)]

    downhill = None

    for (down_y, down_x) in adjacent:
        if down_y in range(len(area)) and down_x in range(len(area[y])) and area[down_y][down_x] < area[y][x]:
            downhill = (down_y, down_x)

    if downhill == None:
        return (y, x)

    return calc_basin(*downhill)

def main():
        
    basins = []
    
    for y in range(len(area)):
        for x in range(len(area[y])):

            location = area[y][x]

            if location != 9:
                basins.append(calc_basin(y, x))          
    
    third_largest = Counter(basins).most_common(3)

    print("Largest basins:", reduce(lambda a, b: a*b, [x[1] for x in third_largest]))

if __name__ == '__main__':
    main()