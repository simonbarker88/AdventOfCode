def main():

    text_file = 'H:\AdventOfCode\Day9.txt'

    with open(text_file,'r') as f:
        area = [[int(char) for char in x if char != "\n"] for x in f.readlines()]
        
    total = 0

    for y in range(len(area)):
        for x in range(len(area[y])):

            location = area[y][x]

            adjacent = [(y-1, x), (y+1, x), (y, x-1), (y, x+1)]

            if all(location < area[y][x] for y, x in adjacent if y in range(len(area)) and x in range(len(area[y]))):
                total+= location + 1           
    
    print('Low points:',total)

if __name__ == '__main__':
    main()