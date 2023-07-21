def Vowels():
    letters = ['A', 'a', 'I', 'i', 'U', 'u', 'E', 'e', 'O', 'o ']
    userInput = [i for i in input("Enter Your Strings : ")]
    for i in letters:
        for j in userInput:
            if i == j:
                userInput[userInput.index(j)] = "!"
    return userInput

print("".join(Vowels()))