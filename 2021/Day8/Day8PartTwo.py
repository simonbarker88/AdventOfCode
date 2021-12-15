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

        three = [x for x in unmatched if len(x - one) == 3][0]
        six = [x for x in unmatched if len(eight - x) == 1 and len(x & one) == 1][0]
        five = [x for x in unmatched if x <= six and len(six - x) == 1][0]
        zero = [x for x in unmatched if x == (eight - four) | one | (eight - three)][0]
        two = [x for x in unmatched if len(x - five) == 2 and len(x & five) == 3][0]
        nine = [x for x in unmatched if x == eight - (six - five)][0]

        mapping = {x: str(i) for i, x in enumerate([zero, one, two, three, four, five, six, seven, eight, nine])}

        total += int("".join(mapping[d] for d in digits))
    
    print(total)

if __name__ == '__main__':
    main()