import pyfiglet
from colorama import Fore
import random

def show():
    for satr in game_board:
        for cell in satr:
            if cell=="X":
                print(cell ,end=" ")
            elif cell == "O":
                print(cell ,end=" ")
            else:
                print(cell, end="  ")
        print()

def chek_game(player1_ch, player2_ch):
    for j in range(3):
        if game_board[j][0] == player1_ch and game_board[j][1] == player1_ch and game_board[j][2] == player1_ch or game_board[0][j] == player1_ch and game_board[1][j] == player1_ch and game_board[2][j] == player1_ch or game_board[0][2] == player1_ch and game_board[1][1] == player1_ch and game_board[2][0] == player1_ch or game_board[0][0] == player1_ch and game_board[1][1] == player1_ch and game_board[2][2] == player1_ch:
            print("player 1 win!")
            exit()
        if game_board[j][0] == player2_ch and game_board[j][1] == player2_ch and game_board[j][2] == player2_ch or game_board[0][j] == player2_ch and game_board[1][j] == player2_ch and game_board[2][j] == player2_ch or game_board[0][2] == player2_ch and game_board[1][1] == player2_ch and game_board[2][0] == player2_ch or game_board[0][0] == player2_ch and game_board[1][1] == player2_ch and game_board[2][2] == player2_ch:
            print("player 2 win!")
            exit()

def player_player():
    player1_ch = input("player1: enter a character: ")
    player2_ch = input("player2: enter a character: ") 

    k = 0
    while True:
        if k == 9:
            print("DRAW")
            exit()

        print("player 1")
        while True:
            satr = int(input("satr: "))
            soton = int(input("soton: "))

            if 1 <= satr <= 3 and 1 <= soton <= 3: 
                if game_board[satr-1][soton-1] == "-":
                    k = k + 1
                    game_board[satr-1][soton-1] = Fore.RED + player1_ch
                    break
                else:
                    print("khone por hast")
                    print("dobare emtehan kon")
            else:
                print("beyn 0 ta 2 entkhab kon :/")
        show()
        chek_game(Fore.RED + player1_ch, Fore.BLUE + player2_ch)

        if k == 9:
            exit()

        print("player 2")
        while True:
            satr = int(input("satr: "))
            soton = int(input("soton: "))

            if 1 <= satr <= 3 and 1 <= soton <= 3:
                if game_board[satr-1][soton-1] == "-":
                    k = k + 1
                    game_board[satr-1][soton-1] = Fore.BLUE + player2_ch
                    break
                else:
                    print("khone por hast")
                    print("dobare emtehan kon")
            else:
                print("beyn 0 ta 2 entkhab kon :/")

        show()
        chek_game(Fore.RED + player1_ch, Fore.BLUE + player2_ch)

def player_CPU():
    player1_ch = input("player1: enter a character: ")
    player2_ch = "O"

    l = 0
    while True:
        if l == 9:
            print("DRAW")
            exit()

        print("player 1")
        while True:
            satr = int(input("satr: "))
            soton = int(input("soton: "))

            if 1 <= satr <= 3 and 1 <= soton <= 3: 
                if game_board[satr-1][soton-1] == "-":
                    l = l + 1
                    game_board[satr-1][soton-1] = Fore.RED + player1_ch
                    break
                else:
                    print("khone por hast")
                    print("dobare emtehan kon")
            else:
                print("beyn 0 ta 2 entkhab kon :/")
        show()
        chek_game(Fore.RED + player1_ch, Fore.BLUE + player2_ch)

        if l == 9:
            print("DRAW")
            exit()

        print("player 2")
        while True:
            satr = random.randint(0,2)
            soton = random.randint(0,2)

            if game_board[satr][soton] == "-":
                l = l + 1
                game_board[satr][soton] = Fore.BLUE + player2_ch
                break
            
            else:
                print("khone por hast")
                print("dobare emtehan kon")
    
        show()
        chek_game(Fore.RED + player1_ch, Fore.BLUE + player2_ch)


title = pyfiglet.figlet_format("Tic Tac Toe", font="slant")
print(title)

game_board = [["-","-","-"],
              ["-","-","-"],
              ["-","-","-"]]

show()

game_mod = input("player_player or player_CPU: ")

if game_mod == "player_player":
    player_player()
if game_mod == "player_CPU":
    player_CPU()