input_file = open("04_input.txt", "r")
lines = input_file.read().split('\n')
print('Number of inputs: ', len(lines))

# Grab input sequence
inputs = lines[0].split(',')
# print(inputs)

# Grab board data
boards = []
board = []
for line in lines[1:]:
    # print(line)
    if line == '' and len(board)>0:
        boards.append(board)
        board = []
        continue
    board.extend(a for a in line.strip().split(' ') if len(a)>0)
boards.append(board)

# print(boards)
num_boards, dim_boards = len(boards), len(boards[5])
print('number of boards: ', num_boards)
print('items per board: ', dim_boards)

# initialise hit/miss list
hitmiss = [ [False for i in range(dim_boards)] for i in range(num_boards)]

def update_boards (boards, hitmiss, number):
    '''based on number, update hitmiss to true for the number that tio'''
    for n, board in enumerate(boards):
        for x, num in enumerate(board): #loop each number in board
            if num == number:
                hitmiss[n][x]=True
                continue # break the one board loop if found match

def print_board(bored):
    '''rearranges flat list into 5x5 grid and print'''
    for i in range(5):
        printable = bored[5*i:5*i+5]
        print(printable)

def check_win(hitmiss):
    '''function to check each board for wins...'''
    def check_rows(board):
        rows = [board[5*i:5*i+5] for i in range(5)]
        # print('rows',rows)
        out = [sum(row) for row in rows]
        # print('rowsums:', out)
        return max(out)

    def check_cols(board):
        cols = [[board[5*i+j] for i in range(5)] for j in range(5)]
        # print('cols', cols)
        out = [sum(col) for col in cols ]
        # print('colsums:', out)
        return max(out)

    def check_diag(board):
        diag1 = sum([board[6*i] for i in range(5)])
        diag2 = sum([board[4*i] for i in range(5)])
        # print('diagsums:', max(diag1,diag2)) 
        return max(diag1,diag2)

    winners = []
    for i,b in enumerate(hitmiss):
        # print_board(b)
        score = max(check_rows(b), check_cols(b),check_diag(b))
        if score == 5:
            winners.append(i)
    if len(winners) >0: return winners
    else: return None

def calculate_score(winner_board, winner_hitmiss, lastnum):
    score = 0
    for i, hit in enumerate(winner_hitmiss):
        print(winner_board[i])
        if not hit: score+=int(winner_board[i])
    score *= int(lastnum)
    return score
    
for i, inp in enumerate(inputs):
    update_boards(boards,hitmiss,inp)
    winner = check_win(hitmiss)
    if winner:
        winner = winner[0]
        winner_score = calculate_score(boards[winner], hitmiss[winner], inp)
        break
print('score of first winning board is ', winner_score)

for i, inp in enumerate(inputs):
    update_boards(boards,hitmiss,inp)
    winner = check_win(hitmiss)
    if winner and len(boards) ==1:
        last_winner_score = calculate_score(boards[0], hitmiss[0], inp)
    if winner:
        for winner_idx in sorted(winner,reverse=True):
            boards.pop(winner_idx)
            hitmiss.pop(winner_idx)
            
print('last winner score is', last_winner_score)
