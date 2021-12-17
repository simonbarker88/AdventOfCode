syntax_scores = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

def main():

    text_file = 'H:\AdventOfCode\Day10.txt'

    with open(text_file,'r') as f:
        lines = f.readlines()
            
    corrupted = []
    
    for line in lines:
        while True:
            no_changes = line
            line = line.replace('()','').replace('{}','').replace('[]','').replace('<>','')

            if line == '' or line == no_changes:
                break
        for char in line:
            if char in '}])>':
                corrupted.append(char)
                break
        
        print(line)

    print('Syntax error scrore:',sum(map(syntax_scores.get,corrupted)))

if __name__ == '__main__':
    main()