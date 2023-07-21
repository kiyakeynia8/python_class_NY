def space(n, s):
    for i in range(int(((n * 2 - 1) - s)/2)):
        print(" ",end="")
def lozee(n):
    s = 1
    o = "+"
    for i in range(2):
        for a in range(n):
            print("\n")
            space(n, s)
            for i in range(s):
                print("*",end="")
            space(n, s)
            if o == "+":
                s += 2
            elif o == "-":
                s -= 2
        s = n * 2 - 3
        o = "-"
lozee(int(input("enter a numebr: ")))