import random
import pyfiglet

title = pyfiglet.figlet_format("&--Dise--&", font="slant")
print(title)

dise_number = 0
sum_numbers = 0
c = 0

while dise_number != 6:
    dise_number = random.randint(1,6)
    c += 1
    print(f"number {c} = {dise_number}")
    sum_numbers += dise_number

print("sum = ",sum_numbers)