def capital_or_small(string):
    c = 0
    s = 0
    for ch in string:
        for i in range(65, 91):
            if ch == i:
                c += 1
        for i in range(97, 123):
            if ch == i:
                s += 1
    return c, s

string = input("enter a string: ")
print("capital:",capital_or_small(string)[0],"small:",capital_or_small(string)[1])