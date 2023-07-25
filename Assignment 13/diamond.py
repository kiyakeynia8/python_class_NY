ran = int(input("ernter a number(odd numbers): "))
x = [0,ran,1]
for i in range(2):
    for i in range(x[0],x[1],x[2]):
        print(((ran - i) * "  "), ((i * 2 - 1) * "🤍"), ((ran - i) * "    "), ((i * 2 - 1) * "🤍"))
    x = [ran, 0, -1]