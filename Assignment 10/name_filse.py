names = input("enter a list of file names(test.py turtle.py test.ipynb): ")

names = names.split(" ")

for name in names:
    f = 0
    c = 0
    if "." in name:
        p = name.split(".")
        for i in ("0","1","2","3","4","5","6","7","8","9"):
            if i in p[1]:
                print(f"There is a number in the {name} suffix")
                f += 1
                break

        if len(p[1]) == 1 or len(p[1]) > 3:
            print(f"The problem is in the number of letters in the suffix of the {name}")
            f += 1
        
        elif p[1] == "err":
            print(f"The {name} suffix is equal to 'err'")
            f += 1

    else:
        print(f"in {name} '.' not find")
        f += 1
    
    for i in ("0","1","2","3","4","5","6","7","8","9"):
        c += name.count(i)
        if c > 3:
            print(f"There are more than 3 numbers in the {name}")
            f += 1
            break

    for i in ("0","1","2","3","4","5","6","7","8","9"): 
        if name[0] == i:
            print(f"name {name} starts with a number")
            f += 1
    
    if f == 0:
        print(f"{name} is acceptable")
    else:
        print(f"{name} is not acceptable")