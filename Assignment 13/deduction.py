op = int(input("1=sum, 2=sub, 3=mul, 4=div\n"))

def show(a,b):
    print("  "+str(a)+ "\n-----\n  "+ str(b))

def mul(d1, d2):
    result_s = d1["s"] * d2["s"]
    result_m = d1['m'] * d2['m']
    return result_s , result_m

def sub(d1, d2):
    result_s = (d1["s"] * d2["m"]) - (d2["s"] * d1["m"])
    result_m = d1["m"] * d2["m"]
    return result_s , result_m

def sum(d1, d2):
    result_s = (d1["s"] * d2["m"]) + (d2["s"] * d1["m"])
    result_m = d1["m"] * d2["m"]
    return result_s , result_m

def div(d1, d2):
    if d2['m'] != 0 and d2["s"] != 0:
        result_s = d1["s"] * d2["m"]
        result_m = d1["m"] * d2["s"]
        return result_s , result_m
    else:
        return "numerator or denominator are equal to 0"

for i in range(2):
    s = int(input("enter numerator: "))
    m = int(input("enter denumerator: "))
    if i == 0:
        dct1  = {"s":s, "m":m}
    else:
        dct2 = {"s":s, "m":m}

if op == 1:
    a , b = sum(dct1, dct2)
    show(a,b)

elif op == 2:
    a , b = sub(dct1, dct2)
    show(a,b)

elif op == 3:
    a , b = mul(dct1, dct2)
    show(a,b)

elif op == 4:
    a , b = div(dct1, dct2)
    show(a,b)