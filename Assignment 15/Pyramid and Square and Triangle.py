class Triangle:
    def __init__(self, h, b, s1, s2):
        self.h = h
        self.b = b
        self.s1 = s1
        self.s2 = s2

    def area(self):
        return (0.5 * self.b) * self.h

    def environment(self):
        return self.s1 + self.s2 + self.b
    
class Square:
    def __init__(self, z):
        self.z = z

    def area(self):
        return self.z ** 2

    def environment(self):
        return 4 * self.z

class Pyramid:
    def __init__(self, t, a, e):
        self.t = t
        self.a = a
        self.e = e
    
    def Volume(self):
        return self.e * self.a * (self.t / 3)