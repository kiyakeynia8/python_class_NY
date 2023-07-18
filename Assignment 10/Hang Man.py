import random

words = [["Soccer", "Volleyball", "handball", "basketball", "Swim", "Running", "boxing", "skate", "skateboard", "tennis"], 
    ["cat", "dog", "Horse", "mouse", "Rabbit", "Wolf", "Bear", "Lion", "Goat", "sheep"],
    ["apple", "banana", "Orange", "Apricot", "Peach", "pear", "mango", "Pineapple", "Strawberry", "Mulberry"],
    ["red", "green", "blue", "white", "Black", "Cyan", "indigo", "Gray", "Dark blue", "Dark green"],
    ["kiya", "sara", "ali", "mohamad", "javad", "reza", "nima", "alireza", "kian", "ahmad"]]

safcn = int(input("1= sports\n2= animals\n3= fruits\n4= colors\n5= names\n"))
word = random.choice(words[safcn-1])
user_w = ["-" for i in range(len(word))]
h = ["💙" for i in range(int(len(word) * 1.5))]
f = []

while True:
    u_w = "".join(user_w)
    u_h = "".join(h)
    print(u_w)
    print(u_h)

    if str(u_w) == word:
        print("you winnnn!!")
        break

    w = input("enter your Guess: ")
    w = w.lower()
    
    if w in f:
        print("You already guessed it")

    for i in range(len(word)):
        if word[i] == w:
            user_w[i] = w
            f.append(w)

    if w not in word:
        if w in f:
            print("You already guessed it")
        else:
            h = h[0:len(h)-1]
            f.append(w)
    
    if len(h) == 0:
        print("You lose!!!")
        break