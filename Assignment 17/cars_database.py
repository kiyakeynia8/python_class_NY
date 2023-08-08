import sqlite3

data = sqlite3.connect("cars_database.db")
c = data.cursor()

def csv_to_database(c):
    data_csv = open("cars_dataset.csv", "r")
    
    try:
        c.execute("""CREATE TABLE cars (
            Car TEXT,
            MPG TEXT,
            Cylinders TEXT,
            Displacement TEXT,
            Horsepower TEXT,
            Weight TEXT,
            Acceleration TEXT,
            Model TEXT,
            Origin TEXT
        )
    """)
    except:
        pass

    datas = []

    a = 1
    for i in data_csv.readlines():
        if a == 1:
            a = 2
            continue
        i = i.rstrip().split(",")
        datas.append(tuple(i))

    for i in datas:
        c.execute(f"INSERT INTO cars VALUES {i}")

    data.commit()
csv_to_database(c)

class Car:
    def __init__(self, data):
        self.data = data

    def show_japanese_cars(self):
        a = []
        for i in self.data.execute("SELECT * FROM cars WHERE Origin == 'Japan'"):
            a.append(i[0])
        return a

    def longest_name(self):
        l = ""
        for i in self.data.execute("SELECT Car FROM cars"):
            i = i[0]
            if len(i) > len(l):
                l = i
        
        return l

    def shortest_name(self):
        l = self.longest_name()
        for i in self.data.execute("SELECT Car FROM cars"):
            i = i[0]
            if len(i) < len(l):
                l = i
        
        return l

    def average_cylinders(self):
        c = []
        for i in self.data.execute("SELECT Cylinders FROM cars"):
            i = i[0]
            c.append(int(i))
        
        return sum(c) / len(c)

    def average_horsepower(self):
        p = []
        for i in self.data.execute("SELECT Horsepower FROM cars"):
            i = i[0]
            p.append(float(i))
        
        return sum(p) / len(p)

    def light_cars(self):
        l = []
        f = 0
        for i in self.data.execute("SELECT * FROM cars ORDER BY Weight"):
            i = i[0]
            l.append(i)
            f += 1
            if f == 50:
                return l

car = Car(c)

while True:
    op = int(input("1= Show Japanese cars, 2= longest name, 3= shortest name, 4= Average cylinders, 5= average horsepower, 6= light cars, 7= exit\n"))

    if op == 1:
        print(car.show_japanese_cars())
    
    elif op == 2:
        print(car.longest_name())
    
    elif op == 3:
        print(car.shortest_name())

    elif op == 4:
        print(car.average_cylinders())

    elif op == 5:
        print(car.average_horsepower())

    elif op == 6:
        print(car.light_cars())
    
    elif op == 7:
        data.close()
        break