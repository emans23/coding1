import math
class Circle:
    def __init__(self, radius):
        self.radius = radius  
    def calculate_area(self):
        return math.pi * self.radius ** 2
    def calculate_perimeter(self):
        return 2 * math.pi * self.radius
if __name__ == "__main__":
    circle1 = Circle(5)
    print(f"Radius: {circle1.radius}")
    print(f"Area: {circle1.calculate_area():.2f}")
    print(f"Perimeter: {circle1.calculate_perimeter():.2f}")