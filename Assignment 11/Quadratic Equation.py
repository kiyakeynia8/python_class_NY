import math

def Equation(a,b,c):
    num = ((b ** 2) - ((4 * a) * c))
    if num > 0:
        l = []
        s = "+"
        m = (math.sqrt(num))
        for i in range(2):
            str = f"(({b} * -1) {s} {m}) / (2 * {a})"
            str = eval(str)
            l.append(str)
            s = "-"
        return l
    elif num == 0:
        result_1 = ((b * -1) / (2 * a))
        return result_1

a = float(input("enter number 1:"))
b = float(input("enter number 2:"))
c = float(input("enter number 3:"))

print(Equation(a,b,c))