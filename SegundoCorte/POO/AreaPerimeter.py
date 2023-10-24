class Circle:
    
    pi = 3.14
    
    def __init__(self, diameter):
        print('Creating circle with diameter: {d}'.format(d = diameter))
        self.radius = diameter / 2
        
    def area(self):
        return self.pi * (self.radius) ** 2
        
    def perimeter(self):
        return 2*self.pi*self.radius
        
circle = Circle(1)
area = circle.area()
perimeter = circle.perimeter()

print('Area: ', area , ', Perimeter: ', perimeter)
print()

class Square:
    
    def __init__(self, side):
        print('Creating square with side: {s}'.format(s = side))
        self.side = side
        
    def area(self):
        return self.side**2
        
    def perimeter(self):
        return 4 * self.side

square = Square(2)
area = square.area()
perimeter = square.perimeter()

print('Area: ', area , ', Perimeter: ', perimeter)
print()

class Rectangle:
    
    def __init__(self, base, high):
        print('Creating rectangle with base: {b}'.format(b = base) + ' and high: {h}'.format(h = high))
        self.base = base
        self.high = high 
        
    def area(self):
        return self.base * self.high
        
    def perimeter(self):
        return 2 * self.base + 2 * self.high 

rectangle = Rectangle(2,5)
area = rectangle.area()
perimeter = rectangle.perimeter()

print('Area: ', area , ', Perimeter: ', perimeter)
print()

class Triangle:
    
    def __init__(self, base, high):
        print('Creating Triangle with base: {b}'.format(b = base) + ' and high: {h}'.format(h = high))
        self.base = base
        self.high = high
        hipo = (base**2+high**2)**0.5
        self.hipo = hipo
        
    def area(self):
        return (self.base * self.high)/2 
        
    def perimeter(self):
        return self.base + self.high + self.hipo  

triangle = Triangle(2,5)
area = triangle.area()
perimeter = triangle.perimeter()

print('Area: ', area , ', Perimeter: ', perimeter)
print()
