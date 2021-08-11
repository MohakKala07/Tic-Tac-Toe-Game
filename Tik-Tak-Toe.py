player_1=""
player_2=""
flag=""#to check
game_on = True
winner = None
entry = "X"  #to handle X & O
play_board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]#to store horizontal lines of board
def to_play_game():#basically the main function
    to_enter_name()#to enter name of players
    to_check_name()#to check validity of name
    to_place_board()#to display the Board
    while game_on:# the main loop which runs all basically
        to_handle_turn(entry)#this is to handle turn
        to_check_gameresult()#to check result of game
        to_flip_p()#to flip the turn between 2 players
    if winner == "X" :
        print(player_1 + " won.")
    elif winner== "O":
        print(player_2 + " won.")
    elif winner == None:
        print("Tie.")
    z=input("Would like to play again ? (Y/N)")
    if z=='Y':
        to_play_game()
    else:
        print("THANK YOU FOR PLAYING!!")
def to_check_gameresult():
    to_check_winner()
    to_check_tie()
def to_place_board():#this will add vertical lines to the board
    print("\n")
    print(play_board[0] + " | " + play_board[1] + " | " + play_board[2] + "     1 | 2 | 3")
    print(play_board[3] + " | " + play_board[4] + " | " + play_board[5] + "     4 | 5 | 6")
    print(play_board[6] + " | " + play_board[7] + " | " + play_board[8] + "     7 | 8 | 9")
    print("\n")
def to_handle_turn(p):
    print(p + "'s turn.")
    pos = input("Choose a pos from 1-9: ")
    valid = False
    while not valid:
        while pos not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            pos = input("Choose a pos from 1-9: ")
        pos = int(pos) - 1
        if play_board[pos] == "-":
            valid = True
        else:
            print("You can't go there. Go again.")
    play_board[pos] = p
    to_place_board()
def to_enter_name():
    global player_2
    global player_1
    player_1 = input("Enter a name for the X player:")
    player_2 = input("Enter a name for the 0 player:")
def to_check_name():
    global entry
    flag = input("Who plays first" + " " + player_1 + " or " + player_2 + "?")
    for i in range(1, 100, 1):
        print(flag+","+player_1)
        if flag!=player_1 and flag!=player_2:
            print(flag + "is not a registered player")
        else:
            break
        flag = input("Who plays first " + player_1 + " or " + player_2 + "?")
    if flag == player_1:
        entry = "X"
    elif flag == player_2:
        entry = "O"  
def to_check_tie():
    global game_on
    if "-" not in play_board:
        game_on = False
        return True
    else:
        return False 
def to_check_winner():
    global winner
    row_win = to_check_rows()
    column_win = to_check_columns()
    diagonal_win = to_check_diagonals()
    if row_win:
        winner = row_win
    elif column_win:
        winner = column_win
    elif diagonal_win:
        winner = diagonal_win
    else:
        winner = None
def to_check_columns():
    global game_on
    col_1 = play_board[0] == play_board[3] == play_board[6] != "-"
    col_2 = play_board[1] == play_board[4] == play_board[7] != "-"
    col_3 = play_board[2] == play_board[5] == play_board[8] != "-"
    if col_1 or col_2 or col_3:
        game_on = False
    if col_1:
        return play_board[0]
    elif col_2:
        return play_board[1]
    elif col_3:
        return play_board[2]
    else:
        return None
def to_check_rows():
    global game_on
    row_1 = play_board[0] == play_board[1] == play_board[2] != "-"
    row_2 = play_board[3] == play_board[4] == play_board[5] != "-"
    row_3 = play_board[6] == play_board[7] == play_board[8] != "-"
    if row_1 or row_2 or row_3:
        game_on = False
    if row_1:
        return play_board[0]
    elif row_2:
        return play_board[3]
    elif row_3:
        return play_board[6]
    else:
        return None
def to_check_diagonals():
    global game_on
    diagonal_1 = play_board[0] == play_board[4] == play_board[8] != "-"
    diagonal_2 = play_board[2] == play_board[4] == play_board[6] != "-"
    if diagonal_1 or diagonal_2:
        game_on = False
    if diagonal_1:
        return play_board[0]
    elif diagonal_2:
        return play_board[2]
    else:
        return None
def to_flip_p():
    global entry
    if entry == "X":
        entry = "O"
    elif entry == "O":
        entry = "X"
to_play_game()