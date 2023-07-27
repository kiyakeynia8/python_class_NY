a_1 = float(input("enter a : "))
b_1 = float(input("enter b : "))
a_2 = float(input("enter a : "))
b_2 = float(input("enetr b : "))

dict = {"a1": a_1, "b1": b_1, "a2": a_2, "b2": b_2} 

def sum(dict):
    return f"{dict['a1'] + dict['a2']}, {dict['b1'] + dict['b2']}"

def sub(dict):
    return f"{dict['a1'] - dict['a2']}, {dict['b1'] - dict['b2']}"

op = int(input("1= sum, 2= sub\n"))

if op == 1:
    print(sum(dict))
elif op == 2:
    print(sub(dict))