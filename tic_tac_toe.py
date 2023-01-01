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