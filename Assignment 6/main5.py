str = input("enter your Sentence: ")

str = str.split()
str = str[::-1]
str = "*".join(str)

print(str)