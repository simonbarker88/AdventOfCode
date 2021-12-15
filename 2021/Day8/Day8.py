def main():

    text_file = 'H:\AdventOfCode\Day8.txt'

    with open(text_file,'r') as f:
        lines = f.readlines()

    total = 0

    for line in lines:
        sequences, digits = line.split(" | ")

        sequences = [frozenset(letters) for letters in sequences.split()]
        digits = [frozenset(letters) for letters in digits.split()]
        
        one, seven, four, *unmatched, eight = sorted(set(sequences), key=len)

        total += sum(x in {one, four, seven, eight} for x in digits)
    
    print('Number of 1,4,7 or 8 digits:',total)

if __name__ == '__main__':
    main()