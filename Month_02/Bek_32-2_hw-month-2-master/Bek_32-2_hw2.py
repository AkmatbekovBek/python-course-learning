class Figure:
    def __init__(self):
        self.unit = 'cm'

    def calculate_area(self):
        pass

    def info(self):
        pass

class Circle(Figure):
    def __init__(self, radius):
        super(Circle, self).__init__()
        self.__radius = radius


    def calculate_area(self):
        return 3.14 * self.__radius ** 2

    def info(self):
        print( f'Circle radius: {self.__radius}{self.unit},' 
               f' area: {self.calculate_area()}{self.unit}' )

# circle = Circle(2)
# circle.calculate_area()
# circle.info()



class RightTriangle(Figure):
    def __init__(self, side_a, side_b):
        super(RightTriangle, self).__init__()
        self.__side_a = side_a
        self.__side_b = side_b

    def calculate_area(self):
        return (self.__side_a * self.__side_b) / 2

    def info(self):
        print(f'Right Triangle side a: {self.__side_a}{self.unit}, side b: {self.__side_b}{self.unit},'
              f' area: {self.calculate_area()}{self.unit}')

# triangle = RightTriangle(5, 8)
# triangle.calculate_area()
# triangle.info()




circle1 = Circle(10)
circle2 = Circle(2)
triangle1 = RightTriangle(5, 8)
triangle2 = RightTriangle(10, 15)
triangle3 = RightTriangle(12, 21)

list_of_figuries = [circle1, circle2, triangle1, triangle2, triangle3]
for figure in list_of_figuries:
    figure.info()


