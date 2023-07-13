import random

while True:
    a = int(input("To exit the game input -1 otherwise input -2 -> "))
    number_y = int(input("enter your number : "))
    bigـnumber = 100
    small_number = 0
    if a == -1:
        break
    while True:
        number = random.randint(small_number, bigـnumber)
        print("computer number = ",number)

        if number_y == number:
            print("computer win")
            break

        s = int(input("up = 1 \n down = 2 \n"))
        
        if s == 1:
            small_number = number + 1
        
        elif s == 2:
            bigـnumber = number - 1