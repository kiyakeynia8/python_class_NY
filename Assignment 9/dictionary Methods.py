import random
import pyfiglet

title = pyfiglet.figlet_format(" -   car   -   - store -", font="banner3-D") # 5lineoblique, 3-d, slant, banner3-D
print(title)

name_cars = ["Abadal","Aixam","Alfa Romeo","Ascari","Askam","Audi Sport","Austin","Autobacs","Brabus","Brammo","Brilliance","Bristol","Changfeng","Chery","Chevrolet Corvette","DeSoto","Detroit Electric","Devel Sixteen","Diatto","DINA","DKW","DMC","Dodge","Dodge Viper","Dongfeng","Donkervoort","Drako","DS","Duesenberg"]
color_cars = ["red","orange","yellow","green","blue","indigo","violet","purple","pink","silver","gold","beige","brown","gray","black","white"]
max_speed_cars = [180,185,190,195,200,205,210,215,220,225,230,235,240,245,250]

cars_info = {}

for i in range(len(name_cars)):
    cars_info.update({f"name{i}" : f"{name_cars[i]}"})
    color = random.choice(color_cars)
    cars_info.update({f"color {name_cars[i]}" : f"{color}"})
    speed = random.choice(max_speed_cars)
    cars_info.update({f"speed {name_cars[i]}" : f"{speed}"})

while True:
    print("""1 -> keys
2 -> values
3 -> show all
4 -> clear
5 -> find
6 -> del item
7 -> exit
""")
    a = int(input())
    if a == 1:
        print("keys")
        print(cars_info.keys(), end=",")

    elif  a == 2:
        print("values")
        print(cars_info.values(), end=",")
    
    elif a == 3:
        print("items")
        print(cars_info.items())
    
    elif a == 4:
        cars_info.clear()
        print("clear successfully!!")

    elif a == 5:
        b = input("key: ")
        print(cars_info.get(b))
    
    elif a == 6:
        b = input("key: ")
        cars_info.pop(b)
        print("delet successfully!!")

    elif a == 7:
        break

print("bayyy")