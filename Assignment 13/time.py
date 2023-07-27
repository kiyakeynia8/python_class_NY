op = int(input("1=sub, 2=sum\n"))

for i in range(2):
    hour = int(input("enter hours: "))
    minut = int(input("enter minuts: "))
    second = int(input("enter seconds: "))
    if i == 0:
        time1_dict = {"hour":hour,
                    "minut":minut,
                    "second":second}
    else:
        time2_dict = {"hour":hour,
                    "minut":minut,
                    "second":second}

def show(h,m,s):
    return f"{h}:{m}:{s}"

def check(h,m,s):
    while not(0 <= s <= 60 and 0 <= m <= 60):
        if s >= 60:
            s -= 60
            m += 1
        if s < 0:
            m -= 1
            s += 60
        if m >= 60:
            m -= 60
            h += 1
        if m < 0:
            h -= 1
            m += 60
    return h,m,s

def operation(time1_dict, time2_dict, d):
    h = eval(f"{time1_dict['hour']} {d} {time2_dict['hour']}")
    m = eval(f"{time1_dict['minut']} {d} {time2_dict['minut']}")
    s = eval(f"{time1_dict['second']} {d} {time2_dict['second']}")
    h,m,s = check(h,m,s)
    return show(h,m,s)

if op == 1:
    d = "-"
    print(operation(time1_dict, time2_dict, d))

elif op == 2:
    d = "+"
    print(operation(time1_dict, time2_dict, d))