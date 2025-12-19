from math import pi

class Shape:
    def __init__(self, name):
        self.name = name

class Rectangle(Shape):
    def __init__(self, name, length, width):
        self.length = length
        self.width = width
        super().__init__(name)
    
    def area(self):
        return self.length * self.width
    
class Circle(Shape):
    def __init__(self, name, radius):
        self.radius = radius
        super().__init__(name)

    def area(self):
        return pi * self.radius * self.radius

# Function to get user input for rectangle details
def get_rectangle_details():
    name = input("Enter rectangle name: ")
    length = float(input("Enter rectangle length: "))
    width = float(input("Enter rectangle width: "))
    return Rectangle(name, length, width)

# Function to get user input for circle details
def get_circle_details():
    name = input("Enter circle name: ")
    radius = float(input("Enter circle radius: "))
    return Circle(name, radius)

# Take user input to choose which shape details they want to enter
print("Options:")
print("1. Enter rectangle details")
print("2. Enter circle details")
option = int(input("Enter your choice (1/2): "))

# Based on the user's choice, get the respective details
if option == 1:
    rectangle = get_rectangle_details()
    print("Rectangle details:")
    print("Name:", rectangle.name)
    print("Length:", rectangle.length)
    print("Width:", rectangle.width)
    print("Area:", rectangle.area())
elif option == 2:
    circle = get_circle_details()
    print("Circle details:")
    print("Name:", circle.name)
    print("Radius:", circle.radius)
    print("Area:", circle.area())
else:
    print("Invalid option selected")
