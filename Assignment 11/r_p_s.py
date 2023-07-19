import random
import pyfiglet

title = pyfiglet.figlet_format("rock  paper  scissors", font="5lineoblique") # 5lineoblique, 3-d, slant, banner3-D
print(title)

a = int(input("1 = 1player, 2 = 2player"))
c = int(input("1 or 3 or 5? "))
computer_c = 0
user_c = 0
user2_c = 0
rps = ["rock","paper","scissors"]

def check_1player(b, user_c, computer_c):
    if b == "user":
        user_c += 1
        return "user win!!", user_c, computer_c
    elif b == "computer":
        computer_c += 1
        return "computer win",user_c , computer_c
    else:
        return "draw",user_c , computer_c
    
def check2_1player(user,computer ,a):
        if user == "rock":
            a = {"scissors" : "user", "paper" : "computer", "rock" : "draw"}
            for j in a:
                if computer == j:
                    b = a.get(j)
                    return b
                
        elif user == "paper":
            a = {"scissors" : "computer", "paper" : "draw", "rock" : "user"}
            for j in a:
                if computer == j:
                    b = a.get(j)
                    return b

        elif user == "scissors":
            a = {"scissors" : "draw", "paper" : "user", "rock" : "computer"}
            for j in a:
                if computer == j:
                    b = a.get(j)
                    return b

def check_2player(b, user_c, user2_c):
    if b == "user":
        user_c += 1
        return "user win!!", user_c, user2_c
    elif b == "user2":
        user2_c += 1
        return "user2 win", user_c, user2_c
    else:
        return "draw", user_c, user2_c
    
def check2_2player(user,user2 ,a):
    if user == "rock":
        a = {"scissors" : "user", "paper" : "user2", "rock" : "draw"}
        for j in a:
            if user2 == j:
                b = a.get(j)
                return b
            
    elif user == "paper":
        a = {"scissors" : "user2", "paper" : "draw", "rock" : "user"}
        for j in a:
            if user2 == j:
                b = a.get(j)
                return b

    elif user == "scissors":
        a = {"scissors" : "draw", "paper" : "user", "rock" : "user2"}
        for j in a:
            if user2 == j:
                b = a.get(j)
                return b

if a == 1:
    while True:
        if computer_c == c or user_c == c:
            break

        computer = random.choice(rps)
        user = input("rock or paper or scissors \t")
        print(f"computer : {computer} and user : {user} \n")

        print(check_1player(check2_1player(user, computer, a),user_c,computer_c)[0])

        user_c = check_1player(check2_1player(user, computer, a),user_c,computer_c)[1]
        computer_c = check_1player(check2_1player(user, computer, a),user_c,computer_c)[2]

        print(f"user : {user_c} and computer : {computer_c}")

elif a == 2:
    while True:
        if user_c == c or user2_c == c:
            break

        user = input("user : rock or paper or scissors \t")
        user2 = input("user2 : rock or paper or scissors \t")
        print(f"user2 : {user2} and user : {user} \n")

        print(check_2player(check2_2player(user, user2, a),user_c,user2_c)[0])

        user_c = check_2player(check2_2player(user, user2, a),user_c,user2_c)[1]
        user2_c = check_2player(check2_2player(user, user2, a),user_c,user2_c)[2]

        print(f"user : {user_c} and user2 : {user2_c}")