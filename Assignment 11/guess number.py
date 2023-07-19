player = "player 1"
player_ = "player 2"

def check(number, i_number, player, player_):
    if number > i_number:
        return "go up"
        
    elif number < i_number:
        return "go down"
    
    elif number == i_number:
        p = player
        player = player_
        player_ = p
        return "you win \n next player", player, player_

while True:
    print("for exit game input -1")
    number = int(input(f"{player}: enter a number -> "))
    if number == -1:
        break
    while True:
        i_number = int(input(f"{player_}: Guess a number and enter it -> "))
        s = check(number, i_number, player, player_)
        if len(s) == 3:
            print(s[0])
            player = s[1]
            plaeyr_ = s[2]
            break
        else:
            print(s)