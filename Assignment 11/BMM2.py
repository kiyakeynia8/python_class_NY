def BMM(a, b):
    if b == 0:
        return a
    else:
        return BMM(b, a % b)
    
print(BMM(a = int(input("a: ")),b = int(input("b: "))))