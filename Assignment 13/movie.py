data = open("Assignment 13/data.txt", "r").readlines()

def read_data():
    dict = {}
    for d in data:
        data_ = d.rstrip()
        name, imdb = data_.split(" ")
        dict[name] = imdb
    return dict

def add(dict):
    dict.update({input("enter name of movie: ") : str(float(input("entre movie imdb: ")))})
    return dict

def sort_list(dict):
    for i in sorted(dict.keys()):
        print(dict[i], i)

def sort_imdb(dict):
    s_dict = sorted(dict.values(), reverse=True)  
    for i in range(5):
        for j in dict.keys():
            if dict[j] == s_dict[i]:
                print(s_dict[i], j)

def exit_(dict):
    file = open("Assignment 13/data.txt", "w")
    for i in dict.keys():
        str = i + " " + dict[i]+ "\n"
        file.write(str)

dic_d = read_data()

while True:
    op = int(input("1=add, 2=show sort list, 3=show IMDB, 4=exit\n"))
    if op == 1:
        dic_d = add(dic_d)
    elif op == 2:
        sort_list(dic_d)
    elif op == 3:
        sort_imdb(dic_d)
    elif op == 4:
        exit_(dic_d)
        break