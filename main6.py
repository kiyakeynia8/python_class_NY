number = float(input("enter a number: "))

if number < 0:
    print("D")
    exit(0)

elif number % 2 == 0:
    n = number // 10
    n = number - n * 10

    if n >= 6:
        print("A")
    
    elif 4 >= n:
        print("B")

    else:
        print("C")

else:
    print("C")