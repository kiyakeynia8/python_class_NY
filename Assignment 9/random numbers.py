import random

while True:
    n = int(input("n: "))
    if n > 100:
        print("Enter a number smaller than 100")
    else:
        break

numbers = []

while len(numbers) < n:
    number = random.randint(1,100)
    if number in numbers:
        continue
    else:
        numbers.append(number)

print(numbers)