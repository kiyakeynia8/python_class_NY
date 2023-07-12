import random

while True:
    a = int(input("To exit the game input -1 otherwise input -2 -> "))
    bigـnumber = 100
    small_number = 0
    if a == -1:
        break
    while True:
        number = random.randint(small_number, bigـnumber)
        print("computer number = ",number)

        s = int(input("up = 1 \n down = 2 \n win = 3 \n"))
        if s == 1:
            small_number = number
        
        elif s == 2:
            bigـnumber = number

        elif s == 3:
            print("hooooooo!!!")
            break