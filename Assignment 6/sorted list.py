numbers = []

number1 = float(input("enter your number: "))
number2 = float(input("enter your number: "))
number3 = float(input("enter your number: "))
number4 = float(input("enter your number: "))
number5 = float(input("enter your number: "))

numbers.append(number1)
numbers.append(number2)
numbers.append(number3)
numbers.append(number4)
numbers.append(number5)

a = sorted(numbers)
b = a[::-1]
print(a)
print(b)