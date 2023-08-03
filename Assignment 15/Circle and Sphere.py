import math

class Circle:
    def __init__(self, r):
        self.radius = r

    def Area(self):
        return (self.radius ** 2) * math.pi

    def Perimeter(self):
        return (self.radius * 2) * math.pi 
    
class Sphere(Circle):
    def __init__(self, r):
        super().__init__(r)
        
    def Area(self):
        return (self.radius ** 2) * math.pi * 4

circle = Circle(3)
print(circle.Area())
sphere = Sphere(3)