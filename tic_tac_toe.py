board = {11:' ', 12:' ', 13:' ',
         21:' ', 22:' ', 23:' ',
         31:' ', 32:' ', 33:' '}

def board_display():
     print(f"|{board[11]}|{board[12]}|{board[13]}|\n"
           f"|{board[21]}|{board[22]}|{board[23]}|\n"
           f"|{board[31]}|{board[32]}|{board[33]}|\n")

board_display()
while True:
    game_mode = input("Press 'p' if you want to play Player vs Player. \n"
                        "Press 'c' if you want to play vs computer.\n"
                        "For exit press 'q':\n")
    if game_mode.lower() == 'p':
        print("you are in p")
        break
    elif game_mode.lower() == 'c':
        print("you are in c")
        break
    elif game_mode.lower() == 'q':
        print("Goodbye.")
        break
# def pvp():
#