from tqdm import tqdm

string = input("enter your sentence: ")
Letters = ["0","1","2","3","4","5","6","7","8","9"]
c = 0

for i in tqdm(range(len(string))):
    for j in range(len(Letters)):
        if string[i] == Letters[j]:
            c += int(string[i])
        
print(c)