import random

words = [["Soccer", "Volleyball", "handball", "basketball", "Swim", "Running", "boxing", "skate", "skateboard", "tennis"], 
    ["cat", "dog", "Horse", "mouse", "Rabbit", "Wolf", "Bear", "Lion", "Goat", "sheep"],
    ["apple", "banana", "Orange", "Apricot", "Peach", "pear", "mango", "Pineapple", "Strawberry", "Mulberry"],
    ["red", "green", "blue", "white", "Black", "Cyan", "indigo", "Gray", "Dark blue", "Dark green"],
    ["kiya", "sara", "ali", "mohamad", "javad", "reza", "nima", "alireza", "kian", "ahmad"]]

safcn = int(input("1= sports\n2= animals\n3= fruits\n4= colors\n5= names\n"))
word = random.choice(words[safcn-1])
word = word.lower()
user_w = ["-" for i in range(len(word))]
h = ["💙" for i in range(int(len(word) * 1.5))]
f = []

print(word)

def show_h(h):
    u_h = "".join(h)
    return u_h

def show_w(w):
    u_w = "".join(w)
    return u_w

def check(word, w, f, h):
    if str(show_w(user_w)) == word:
        return "you winnnn!!"
    
    if w not in word:
        if w in f:
            return "You already guessed it"
        else:            
            h = h[0:len(h)-1]
            f.append(w)
        
            if len(h) == 0:
                return "You lose!!!"
            
            return 1, h, f

w = ""
while True:
    st = check(word, w, f, h)
    if st != None:
        if st[0] == 1:
            h = st[1]
            f = st[2]
        else:
            print(st)
    
    if st == "you winnnn!!" or st == "You lose!!!":
        break

    print(show_h(h))
    print(show_w(user_w))

    w = input("enter your Guess: ")
    w = w.lower()

    for i in range(len(word)):
        if word[i] == w:
            user_w[i] = w
            f.append(w)