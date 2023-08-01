import math 

class Circle:
    radius = None

    def __init__(self, r):
        self.radius = r

    def get_radius(self):
        return self.radius

    def Area(self):
        return math.pow(self.radius, 2) * math.pi

    def Perimeter(self):
        return 2 * self.radius * math.pi