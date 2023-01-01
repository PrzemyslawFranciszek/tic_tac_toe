board = {11:' ', 12:' ', 13:' ',
         21:' ', 22:' ', 23:' ',
         31:' ', 32:' ', 33:' '}

def board_display():
     print(f"|{board[11]}|{board[12]}|{board[13]}|\n"
           f"|{board[21]}|{board[22]}|{board[23]}|\n"
           f"|{board[31]}|{board[32]}|{board[33]}|\n")


def play():
    while True:
       try:
           x, y = [int(x) for x in input("Type the position (x,y) of field to fill x for row , y for column:\n").split()]
           if x > 0 and x < 4 and y > 0 and y < 4:
               picked_field = int(str(x) + str(y))
               if board[picked_field] == " ":
                   board[picked_field] = "X"
                   board_display()
                   break
           print("Wrong choice. Type again")
           continue
       except (TypeError, ValueError):
           print("Wrong choice. Type again")
           continue

while True:
    game_mode = input("Press 'p' if you want to play Player vs Player. \n"
                        "Press 'c' if you want to play vs computer.\n"
                        "For exit press 'q':\n")
    if game_mode.lower() == 'p':
        board_display()
        player1_choice = input("Player with cross starts. Please type 'x' if you want to start:\n")
        if player1_choice.lower() == 'x':
            print("player 1 starts.")
            play()
        else:
            print("player 2 starts")
    elif game_mode.lower() == 'c':
        board_display()
        break
    elif game_mode.lower() == 'q':
        print("Goodbye.")
        break
# def pvp():
#