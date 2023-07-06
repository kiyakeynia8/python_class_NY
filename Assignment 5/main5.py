number = int(input("enter your number: "))

print("yes" if number % 7 == 0 and exit(0) else "no")
number = number // 7
number *= 7
number += 7
print(number)