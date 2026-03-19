class Figure:
    def __init__(self):
        self.unit = 'cm'
        self.__perimeter = 0
        
    @property
    def perimeter(self):
        return self.__perimeter

    @perimeter.setter
    def perimeter(self, Perimeter):
        self.__perimeter = Perimeter


    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass

    def info(self):
        pass


class Square(Figure):
    def __init__(self, side_length):
        super(Square, self).__init__()
        self.__side_length = side_length

        self.perimeter = self.calculate_perimeter()


    def calculate_area(self):
        return self.__side_length * self.__side_length

    def calculate_perimeter(self):
        return self.__side_length * 4

    def info(self):
        print(f'Square side length: {self.__side_length}{self.unit},'
              f' perimeter: {self.perimeter}{self.unit}, area: {self.calculate_area()}{self.unit}')

class Rectangle(Figure):
    def __init__(self, length, width):
        super(Rectangle, self).__init__()

        self.__length = length
        self.__width = width

        self.perimeter = self.calculate_perimeter()



    def calculate_area(self):
        return self.__length * self.__width

    def calculate_perimeter(self):
        return (self.__length + self.__width) * 2


    def info(self):
        print(f'Rectangle length: {self.__length}{self.unit}, width: {self.__width}{self.unit},'
              f' perimeter: {self.perimeter}{self.unit}, area: {self.calculate_area()}{self.unit}')


kvad1 = Square(5)
kvad2 = Square(25)
rectangle1 = Rectangle(5, 8)
rectangle2 = Rectangle(15, 24)
rectangle3 = Rectangle(35, 14)

list_of_figuries = [kvad1, kvad2, rectangle1, rectangle2, rectangle3]
for figure in list_of_figuries:
    figure.info()

