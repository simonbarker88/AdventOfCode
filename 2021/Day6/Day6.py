def process_day (a):
    return (a -1 if a - 1 >= 0 else 6)

def main():

    text_file = 'H:\AdventOfCode\Day6.txt'

    with open(text_file,'r') as f:
        lines = [int(x) for x in f.readlines()[0].split(',')]

    for day in range(80):

        tmp_lines = lines.copy()
        act_day = day + 1

        state = map(process_day,lines)

        lines = list(state) 
        
        for line in tmp_lines:
            if line == 0:
                lines.append(8)
            
        #print(f'Day - {act_day}',lines)
    
    print('Number of lanternfish: ',len(lines))

if __name__ == '__main__':
    main()