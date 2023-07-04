w = float(input("enter your weight (KG)"))
h = float(input("enter your height (M)"))

BMI = w / (h**2)

print("your BMI =", BMI)

if BMI < 18.5:
    print("thin")

if 18.5 < BMI < 24.9:
    print("normal")

if 25 < BMI < 29.9:
    print("On the verge of obesity")

if 30 < BMI < 34.9:
    print("obesity")

if 35 < BMI:
    print("extreme obesity")