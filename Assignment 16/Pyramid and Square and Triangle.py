class Square:
    def __init__(self, s):
        self.s = s

    def s_area(self):
        return self.s ** 2
    
    def s_environment(self):
        return 4 * self.s

class Triangle:
    def __init__(self, s):
        self.s = s

    def t_area(self):
        return 2 * (self.s ** 2) / 2
    
    def t_environment(self):
        return 3 * self.s

class Pyramid(Triangle, Square):
    def __init__(self, h, s, t):
        self.h = h
        self.s_s = s
        self.s_t = s

    def p_area(self):
        return Square(self.s_s).s_area() + (4 * (Triangle(self.s_t).t_area()))
    
    def p_volume(self):
        return (self.s_s * self.s_t * self.h) / 3

square = Square(5)
triangle = Triangle(4)
pyramid = Pyramid(6, 5, 4)

print("triangle area:", triangle.t_area(), "triangle environment:", triangle.t_environment())
print("square area:", square.s_area(), "square environment:", square.s_environment())
print("pyramid area:", pyramid.p_area(), "pyramid volume:", pyramid.p_volume())