number = int(input("Enter Your Number:"))
result = 0

for i in range(1,number):
    if number % i == 0:
        result += i
    
if result == number:
	print("yes")
else:
	print("no")