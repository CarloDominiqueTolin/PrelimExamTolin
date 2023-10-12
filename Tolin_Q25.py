#Carlo Dominique T. Tolin
#CPE41S6
class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 1/2*self.base*self.height
    
    def perimeter(self):
        return self.base + 2*((self.height**2 + (self.base/2)**2)**(1/2))


x = Triangle(10,20)
print(f'Area of Triangle with base {x.base} units and height {x.height} units is {x.area()} units squared')
print(f'Perimeter of Triangle with base {x.base} units and height {x.height} units is {x.perimeter()} units')
