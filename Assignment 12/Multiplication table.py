def jadval_zarb(n,m):
    for i in range(1,n+1):
        for s in range(1,m+1):
            print(i * s,end = "  ")
        print()

jadval_zarb(int(input("enter x: ")), int(input("enter y: ")))