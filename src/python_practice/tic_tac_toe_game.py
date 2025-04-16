"""
Tic Tac Toe Game (3x3)

This program implements a simple 3x3 Tic Tac Toe game for two players ('O' and 'X').
Players take turns to place their symbols on the board, and the game ends when:
1. A player wins by aligning three symbols in a row, column, or diagonal.
2. The board is full, resulting in a draw.

How to Play:
1. Players take turns entering a number (1-9) to place their symbol.
2. The program validates input and updates the board.
3. The game ends with a winner or a draw.
"""

counter = 0
PLAYER_SYMBOLS = ["O", "X"]
row1 = [' ',' ',' ']
row2 = [' ',' ',' ']
row3 = [' ',' ',' ']

def user_choice():
    choice = input('please enter a number(1-9)\n')
    while not choice.isdigit() or (int(choice) not in range(1,10)):
        if(not choice.isdigit()):
            print('Sorry, your choice is not valid')
        elif(int(choice) not in range(1,10)):
            print('Your choice is not whithin 1 ~ 9')
        choice = input('please enter a number(1-9)')
    return int(choice)

def display_board(row1, row2, row3):
    print(row1)
    print(row2)
    print(row3)

def current_symbol():
    result = PLAYER_SYMBOLS[counter % 2]
    return result

def update_board(index):
    tableSize = 3
    col_index = index % tableSize - 1 # 0 ,1 ,-1
    row_index = index // tableSize # 0, 1, 2
    if col_index == -1:
        row_index -= 1

    rows = [row1, row2, row3]
    if rows[row_index][col_index] != " ": return False

    rows[row_index][col_index] = current_symbol()
    display_board(row1, row2, row3)
    return True 

def check_winner(): 
    rows = [row1, row2, row3]

    for row in rows:      
     if row[0] == row[1] == row[2] and row[0] != " " :
        return f"{current_symbol()} wins"
    for col in range(3):
        if(row1[col] == row2[col] == row3[col] and (row1[col] != " ")):
            return f"{current_symbol()} wins"
    if row1[0] == row2[1] == row3[2] and row1[0] != " ":
       return f"{current_symbol()} wins"
    if row1[2] == row2[1] == row3[0] and row1[2] != " ":
        return f"{current_symbol()} wins"
    if any(" " in row for row in rows):
        return "Game continues"
    return "Drew"

def startGame():
    global counter
    while counter < 9:
        valid_input = False

        while not valid_input:
            user1_choice = user_choice()
            valid_input = update_board(user1_choice)
               
        result = check_winner()
        if result == "Draw":
            print("It's a draw!")
            break
        elif result != "Game continues":
            print(result)
            break

        counter += 1

startGame()


