number = int(input("enter your number: "))

if number == 0:
    print("The number is equal to zero")
    exit(0)

if number < 0:
    number = str(number)[1:]
    number = int(number)

elif len(str(number)) == 1:
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")
    
# print(number, type(number))
e = 0
o = 0
n = number

def sum(n):
    global e
    global o
    a = number - n
    if a == 0:
        ...
    else:
        if a % 2 == 0:
            e += 1
        else:
            o += 1
    return 0 if n == 0 else (n % 10 + sum(n // 10))

print(sum(n))

if e > o:
    print("Even")
elif o > e:
    print("Odd")
else:
    print("equal")