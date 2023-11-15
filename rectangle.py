class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width
    def area(self):
        return self.height * self.width
    def perimeter(self):
        return (self.height + self.width)*2

rec1 = Rectangle(10,5)
print(rec1.area())
print(rec1.perimeter())