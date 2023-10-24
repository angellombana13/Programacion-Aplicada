#Excercise 1

class Circle:
    pi = 3.14
    
    def area(self, radius):
        return Circle.pi * radius**2

circle = Circle()

pizza_area = circle.area(12/2)

teaching_table_area = circle.area(36/2)

round_room_area = circle.area(11460/2)

#Excercise 2

class Circle:
    pi = 3.14
    
    def __init__(self, diameter):
        print('New circle with diameter: {}'.format(diameter))
    
teaching_table = Circle(36)

#Excercise 3
class Circle:
    pi = 3.14
    
    def __init__(self, diameter):
        print('Creating circle with diameter: {d}'.format(d = diameter))
        self.radius = diameter / 2
    def circumference(self):
        return 2*self.pi*self.radius
medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

print(medium_pizza.circumference(), teaching_table.circumference(), round_room.circumference())

#Excercise 4

class Store:
    pass

alternative_rocks = Store()
isabelles_ices = Store()

alternative_rocks.store_name = "Añternative Rocks"
isabelles_ices.store_name = "Isabelle's Ices"
print(isabelles_ices.store_name)
