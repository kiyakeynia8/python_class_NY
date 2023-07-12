from tqdm import tqdm

numebr = int(input("enter a number: "))
l = int(input("output 1 or output 2? "))

if l == 1:
    for i in tqdm(range(numebr,0,-1)):
        for j in range(1,i+1):
            print(j,end="")

        print()

elif l == 2:
    for i in tqdm(range(1,numebr+1)):
        for j in range(1,i+1):
            print(j,end="")

        print()