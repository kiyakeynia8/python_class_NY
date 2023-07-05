str = input("inter your string: ")

# title and is title

# if str.istitle() == False:
#     t_str = str.title()
#     print(f"False!! \n input -> {str} \n output -> {t_str}")

# else:
#     print("True")

# or

# str = f"False!! \n input -> {str} \n output -> {str.title()}" if str.istitle() == False else "True" 
# print(str)

# find

# s = "I found 'Hello' in your string" if str.find("Hello") == 0 else "I didn't find 'Hello' in your string"
# print(s)

# replace

# s = str.replace(" ","-")
# print("I replaced the spaces in your string with '-' \n", s)

# rstrip and lstrip

l_r = input("left or right? ")
s = f"result -> '{str.rstrip()}'" if l_r == "r" else f"result -> '{str.lstrip()}'"
print(s)