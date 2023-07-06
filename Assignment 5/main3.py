number = int(input("enter your number: "))

if number == 0:
    print("The number is equal to zero")
    exit(0)

if number < 0:
    number = abs(number)

elif len(str(number)) == 1:
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")
    
number = str(number)

a = number.count("1")
b = number.count("3")
c = number.count("5")
d = number.count("7")
e = number.count("9")
f = number.count("2")
g = number.count("4")
h = number.count("6")
i = number.count("8")

odd = a + b + c + d + e
even = f + g + h + i

if even > odd:
    print("Even")
elif odd > even:
    print("Odd")
else:
    print("equal")