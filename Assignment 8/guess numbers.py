player = "player 1"
player_ = "player 2"
while True:
    print("for exit game input -1")
    number = int(input(f"{player}: enter a number -> "))
    if number == -1:
        break
    while True:
        i_number = int(input(f"{player_}: Guess a number and enter it -> "))
        
        if number > i_number:
            print("go up")
        
        elif number < i_number:
            print("go down")
        
        elif number == i_number:
            print("you win")
            print("next player")
            p = player
            player = player_
            player_ = p
            break