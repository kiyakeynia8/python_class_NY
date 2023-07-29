def check(h, m, s):
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

class Time:
    def __init__(self, h1, h2, m1, m2, s1, s2):
        self.h1 = h1
        self.h2 = h2
        self.m1 = m1
        self.m2 = m2
        self.s1 = s1
        self.s2 = s2

    def sum(self):
        h, m, s = self.h1 + self.h2, self.m1 + self.m2, self.s1 + self.s2
        h, m, s = check(h, m, s)
        return h,m,s
    
    def sub(self):
        h, m, s = self.h1 - self.h2, self.m1 - self.m2, self.s1 - self.s2
        h, m, s = check(h, m, s)
        return h,m,s

    def show(self, h, m, s):
        print(f"{h}:{m}:{s}")

time1 = input("enter a time:(2:40:25) ")
time2 = input("enter a time:(2:40:25) ")

time = Time(int(time1.split(":")[0]), int(time2.split(":")[0]), int(time1.split(":")[1]), int(time2.split(":")[1]), int(time1.split(":")[2]), int(time2.split(":")[2]))

op = int(input("1=sum, 2=sub\n"))

if op == 1:
    h, m, s = time.sum()
    time.show(h, m, s)
elif op == 2:
    h, m, s = time.sub()
    time.show(h, m, s)