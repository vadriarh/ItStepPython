class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

#Test data
# r1 = Rectangle(5, 10)
# print(r1.area())
# print(r1.perimeter())
