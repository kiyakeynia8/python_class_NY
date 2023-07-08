names = ["ali", "atefe", "reza", "homa", "amir", "fateme"]

n1 = input("enter name 1: ")
nu1 = int(input("enter number 1: "))

n2 = input("enter name 2: ")
nu2 = int(input("enter number 2: "))

n3 = input("enter name 3: ")
nu3 = int(input("enter number 3: "))

names.insert(nu1-1,n1)
names.insert(nu2-1,n2)
names.insert(nu3-1,n3)

print(names)