def BMM():
    a = int(input("enter first numebr: "))
    b = int(input("enter second numebr: "))

    a_ = []
    b_ = []

    for i in range(1, a+1):
        if int(a / i) == a / i:
            a_.append(i)
        
    for i in range(1, b+1):
        if int(b / i) == b / i:
            b_.append(i)

    f = a_ if len(a_) > len(b_) else b_
    for j in f:
        if f == a_:
            if j in b_:
                s = j
        if f == b_:
            if j in a_:
                s = j
    
    return s

print(BMM())