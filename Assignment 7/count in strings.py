string = input("enter your sentence: ")
l = input()
c = 0

for i in range(len(string)):
    if string[i] == l:
        c += 1

print(c)