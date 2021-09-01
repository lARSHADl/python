def grid():
    print("---------")
    print("|", cells[0], cells[1], cells[2], "|")
    print("|", cells[3], cells[4], cells[5], "|")
    print("|", cells[6], cells[7], cells[8], "|")
    print("---------")


turn = 'X'

global X_win
global o_win


def change(a):
    global turn
    if a == 'X':
        turn = 'O'
    else:
        turn = 'X'


def check():
    global X_win
    global o_win
    X_win = cells[0] == cells[1] == cells[2] == 'X' or cells[3] == cells[4] == cells[5] == 'X' or cells[6] == \
            cells[7] == cells[8] == 'X' or cells[0] == cells[3] == cells[6] == 'X' or cells[1] == cells[4] == \
            cells[7] == 'X' or cells[2] == cells[5] == cells[8] == 'X' or cells[0] == cells[4] == cells[
                8] == 'X' or cells[2] == cells[4] == cells[6] == 'X'

    o_win = cells[0] == cells[1] == cells[2] == 'O' or cells[3] == cells[4] == cells[5] == 'O' or cells[6] == \
            cells[7] == cells[8] == 'O' or cells[0] == cells[3] == cells[6] == 'O' or cells[1] == cells[4] == \
            cells[7] == 'O' or cells[2] == cells[5] == cells[8] == 'O' or cells[0] == cells[4] == cells[
                8] == 'O' or cells[2] == cells[4] == cells[6] == 'O'

    if X_win or o_win :
        return True
    else:
        return False


def input_check():

    keep_looping = True
    count = 0
    while keep_looping == True and count < 9:

        all_coordinates = [['1', '1'], ['1', '2'], ['1', '3'], ['2', '1'], ['2', '2'],
                           ['2', '3'], ['3', '1'], ['3', '2'], ['3', '3']]
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


        coordinates = input('Enter the coordinates: ').split()
        if coordinates[0] and coordinates[1] not in numbers:
            print('You should enter numbers!')
        elif coordinates not in all_coordinates:
            print('Coordinates should be from 1 to 3!')
        elif cells[(3 * int(coordinates[0]) + int(coordinates[1]) - 4)] != ' ':
            print('This cell is occupied! Choose another one!')

        else:
            cells[(3 * int(coordinates[0]) + int(coordinates[1]) - 4)] = turn
            change(turn)
            grid()
            count += 1
        if check():
            keep_looping = False


# cells = list(input('Enter cells: ').replace('_', ' '))
cells = [" " for i in range(0, 9)]

grid()


input_check()
if X_win:
    print(" X wins")
elif o_win:
    print(" O wins")
else:
    print("Draw")

