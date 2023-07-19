def KMM():
    a = int(input("enter first numebr: "))
    b = int(input("enter second numebr: "))

    a_ = []
    b_ = []

    i = 1
    while True:
        a_.append(a * i)
        b_.append(b * i)

        if a < b:
            if a * i in b_:
                return a * i

        else:
            if b * i in a_:
                return b * i

        i += 1
        
print(KMM())