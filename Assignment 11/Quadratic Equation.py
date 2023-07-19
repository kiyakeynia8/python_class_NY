def Quadratic_Equation(a, x , b, c):
    return ((a*x)**2) + (b*x) + c

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
x = float(input("x: "))

print(Quadratic_Equation(a, x, b, c))