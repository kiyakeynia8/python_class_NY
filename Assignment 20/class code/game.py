import logic

game_board = logic.start_game()

while True:
    inp = input("press the your command: ")

    if inp == "w":
        game_board, flag = logic.move_up(game_board)
        status = logic.get_current_state(game_board)
        print(status)
        if status == "Game Not Over":
            logic.add_new_2(game_board)
        else:
            break

    elif inp == "s":
        game_board, flag = logic.move_down(game_board)
        status = logic.get_current_state(game_board)
        print(status)
        if status == "Game Not Over":
            logic.add_new_2(game_board)

    elif inp == "a":
        game_board, flag = logic.move_left(game_board)
        status = logic.get_current_state(game_board)
        print(status)
        if status == "Game Not Over":
            logic.add_new_2(game_board)

    elif inp == "d":
        game_board, flag = logic.move_right(game_board)
        status = logic.get_current_state(game_board)
        print(status)
        if status == "Game Not Over":
            logic.add_new_2(game_board)

    else:
        print("Invalid command!")

    for i in game_board:
        print(i)