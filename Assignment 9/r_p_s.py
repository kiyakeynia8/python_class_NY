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

if a == 1:
    while True:
        if computer_c == c or user_c == c:
            break

        computer = random.choice(rps)
        user = input("rock or paper or scissors \t")
        print(f"computer : {computer} and user : {user} \n")
        
        # if user == "rock":
            # if computer == "scissors":
            #     user_c += 1
            #     print("user win!!")
            # elif computer == "paper":
            #     computer_c += 1
            #     print("computer win")
            # else:
            #     print("draw")

        # elif user == "scissors":
        #     if computer == "paper":
        #         user_c += 1
        #         print("user win!!")
        #     elif computer == "rock":
        #         computer_c += 1
        #         print("computer win")
        #     else:
        #         print("draw")
            
        # elif user == "paper":
        #     if computer == "rock":
        #         user_c += 1
        #         print("user win!!")
        #     elif computer == "scissors":
        #         computer_c += 1
        #         print("computer win")
        #     else:
        #         print("draw")

        if user == "rock":
            a = {"scissors" : "user", "paper" : "computer", "rock" : "draw"}
            for j in a:
                if computer == j:
                    b = a.get(j)
                
        elif user == "paper":
            a = {"scissors" : "computer", "paper" : "draw", "rock" : "user"}
            for j in a:
                if computer == j:
                    b = a.get(j)

        elif user == "scissors":
            a = {"scissors" : "draw", "paper" : "user", "rock" : "computer"}
            for j in a:
                if computer == j:
                    b = a.get(j)

        if b == "user":
            user_c += 1
            print("user win!!")
        elif b == "computer":
            computer_c += 1
            print("computer win")
        else:
            print("draw")

        print(f"user : {user_c} and computer : {computer_c}")

elif a == 2:
    while True:
        if user_c == c or user2_c == c:
            break

        user = input("user : rock or paper or scissors \t")
        user2 = input("user2 : rock or paper or scissors \t")
        print(f"user2 : {user2} and user : {user} \n")
        
        if user == "rock":
            a = {"scissors" : "user", "paper" : "user2", "rock" : "draw"}
            for j in a:
                if user2 == j:
                    b = a.get(j)
                
        elif user == "paper":
            a = {"scissors" : "user2", "paper" : "draw", "rock" : "user"}
            for j in a:
                if user2 == j:
                    b = a.get(j)

        elif user == "scissors":
            a = {"scissors" : "draw", "paper" : "user", "rock" : "user2"}
            for j in a:
                if user2 == j:
                    b = a.get(j)

        if b == "user":
            user_c += 1
            print("user win!!")
        elif b == "user2":
            user2_c += 1
            print("user2 win")
        else:
            print("draw")

        print(f"user : {user_c} and user2 : {computer_c}")