from datetime import datetime

birthday = input("enter your birthday(2009/6/26): ")
year, month, day = int(birthday.split("/")[0]), int(birthday.split("/")[1]), int(birthday.split("/")[2])

d_y,d_m,d_d = int(str(datetime.now()).split(" ")[0].split("-")[0]), int(str(datetime.now()).split(" ")[0].split("-")[1]), int(str(datetime.now()).split(" ")[0].split("-")[2])
t_h,t_m,t_s = int(str(datetime.now()).split(" ")[1].split(":")[0]), int(str(datetime.now()).split(" ")[1].split(":")[1]), int(float(str(datetime.now()).split(" ")[1].split(":")[2]))

if d_d < day:
    d_m -= 1
    d_d += 30

if d_m < month:
    d_y -= 1
    d_m += 30

d, w = ((((d_y - year)*12) + (d_m - month)) *30) + (d_d - day), (((((d_y - year)*12) + (d_m - month)) *30) + (d_d - day)) // 7

print("day:", d, "and week:", w)