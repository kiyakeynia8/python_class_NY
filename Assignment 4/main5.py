w = float(input("enter your weight (KG)"))
h = float(input("enter your height (M)"))

BMI = w / (h**2)

print("your BMI =", BMI)

if BMI < 18.5:
    print("under height")

if 18.5 < BMI < 24.9:
    print("normal height")

if 25 < BMI < 29.9:
    print("over height")

if 30 < BMI < 34.9:
    print("obesllty")

if 35 < BMI:
    print("xtreme obeslty")