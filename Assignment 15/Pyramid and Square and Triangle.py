class Triangle:
    def __init__(self, h, b, s1, s2):
        self.h = h
        self.b = b
        self.s1 = s1
        self.s2 = s2

    def t_area(self):
        return (0.5 * self.b) * self.h

    def t_environment(self):
        return self.s1 + self.s2 + self.b
    
class Square:
    def __init__(self, z):
        self.z = z

    def s_area(self):
        return self.z ** 2

    def s_environment(self):
        return 4 * self.z

class Pyramid(Square):
    def __init__(self, t, e):
        super.__init__(t)
        self.t = t
        self.e = e
    
    def p_volume(self):
        return self.e * self.s_area * (self.t / 3)
    
    def p_area(self):
        return ((self.s_environment() * self.e) / 2) + self.s_area()