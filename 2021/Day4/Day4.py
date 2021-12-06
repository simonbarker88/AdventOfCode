import numpy as np

def generate_cards(lines):
    
    numbers = []
    boards = []
    rows = []
    row = []
    new_card = None
    row_count = 0
    
    for line in lines:
    
        if len(line) > 15:
            numbers = [int(x) for x in line.split(',')]
        
        if line == '\n':
            new_card = True
            continue
        
        if new_card == True:
            row = [int(x) for x in line.split()]
            rows.append(row)
            row_count += 1
            
            if row_count == 5:
                boards.append(np.array(rows))
                rows = []
                new_card = False
                row_count = 0

    return numbers,boards

def check_cards(number,boards):
    
    for index,board in enumerate(boards):
        
        #print(f'Checking board {index} for number {number}')
        for row_no,row in enumerate(board):

            for column_no,column in enumerate(row):
                if column == number:
                   board[row_no,column_no] = 0
        
        if is_bingo(board):
            sum = np.sum(board)
            total = sum * number
            print(f'The winner is board {index}. The last number is {number}. Sum is {sum} and total is {total}')
            return True
                          
def is_bingo(card):
    for i in range (5):
        row_zeros=np.count_nonzero(card[i,:])
        col_zeros=np.count_nonzero(card[:,i])
        if not row_zeros or not col_zeros:
            return True
    
    return False              
   
def main():

    text_file = 'H:\AdventOfCode\Day4.txt'

    with open(text_file,'r') as f:
        lines = f.readlines()
    
    numbers,boards = generate_cards(lines)
    
    for number in numbers:
        if check_cards(number,boards):
            break

if __name__ == '__main__':
    main()