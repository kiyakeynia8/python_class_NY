import sqlite3

data = sqlite3.connect("cars_database.db")

c = data.cursor()

data_csv = open("cars_dataset.csv", "r")

try:
    c.execute("""CREATE TABLE cars(
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

for i in data_csv.readlines():
    data = i.rstrip().split(",")
    datas.append(tuple(data))

for i in datas:
    a = f"INSERT INTO cars VALUES {i}"
    c.execute(a)