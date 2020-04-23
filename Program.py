print('---- Welcom to TicTacToe version 1,0 -----')

print('7|8|9')
print('-+-+-')
print('4|5|6')
print('-+-+-')
print('1|2|3')
print('***********************************')

board = {
    '7': ' ', '8': ' ', '9': ' ',
    '4': ' ', '5': ' ', '6': ' ',
    '1': ' ', '2': ' ', '3': ' '
}
player = 1  # first player
total_moves = 0  # counts of moves
end_check = 0

while True:
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

    if total_moves == 9 or end_check == 1:
        break
    while True:  # input from player
        if player == 1:  # choose player
            p1_input = input('player one:')
            if p1_input.upper() in board and board[p1_input.upper()] == ' ':
                board[p1_input.upper()] = 'x'
                player = 2
                break
            else:
                print('invalid input, please try again')
                continue
        else:
            p2_input = input('player two:')
            if p2_input.upper() in board and board[p2_input.upper()] == ' ':
                board[p2_input.upper()] = 'O'
                player = 1
                break
            else:
                print('invalid input, please try again')
                continue
    total_moves += 1
    print('***********************************')


def check():
    # check p1 moves
    # check horizontal win
    if board['7'] == 'x' and board['8'] == 'x' and board['9'] == 'x':
        print('........player one won!!')
        return 1
    if board['4'] == 'x' and board['5'] == 'x' and board['6'] == 'x':
        print('........player one won!!')
        return 1
    if board['1'] == 'x' and board['2'] == 'x' and board['3'] == 'x':
        print('........player one won!!')
        return 1
    # check diagonal
    if board['7'] == 'x' and board['5'] == 'x' and board['3'] == 'x':
        print('........player one won!!')
        return 1
    if board['9'] == 'x' and board['5'] == 'x' and board['1'] == 'x':
        print('........player one won!!')
        return 1
    # check vertical
    if board['7'] == 'x' and board['4'] == 'x' and board['1'] == 'x':
        print('........player one won!!')
        return 1
    if board['8'] == 'x' and board['5'] == 'x' and board['2'] == 'x':
        print('........player one won!!')
        return 1
    if board['9'] == 'x' and board['6'] == 'x' and board['3'] == 'x':
        print('........player one won!!')
        return 1

        # check p2 moves
        # check horizontal win
    if board['7'] == 'O' and board['8'] == 'O' and board['9'] == 'O':
        print('******player one won!*******')
        return 1
    if board['4'] == 'O' and board['5'] == 'O' and board['6'] == 'O':
        print('******player one won!*******')
        return 1
    if board['1'] == 'O' and board['2'] == 'O' and board['3'] == 'O':
        print('******player one won!*******')
        return 1
        # check diagonal
    if board['7'] == 'O' and board['5'] == 'O' and board['3'] == 'O':
        print('******player one won!*******')
        return 1
    if board['9'] == 'O' and board['5'] == 'O' and board['1'] == 'O':
        print('******player one won!*******')
        return 1
        # check vertical
    if board['7'] == 'O' and board['4'] == 'O' and board['1'] == 'O':
        print('******player one won!*******')
        return 1
    if board['8'] == 'O' and board['5'] == 'O' and board['2'] == 'O':
        print('******player one won!*******')
        return 1
    if board['9'] == 'O' and board['6'] == 'O' and board['3'] == 'O':
        print('******player one won!*******')
        return 1
    return 0
