numbers_1 = []

for i in range(10):
    number = float(input("enter a number: "))
    numbers_1.append(number)

print(numbers_1)
numbers_2 = []
c = 0

while c < 10:
    numbers_2.append(numbers_1[c] + 2)
    c += 1

print(numbers_2)