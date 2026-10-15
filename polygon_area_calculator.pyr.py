import math
class Rectangle():
    def __init__(self,width:int,height:int):
        self.__width = width
        self.__height = height

    def set_width(self,width):
        self.__width = width

    def set_height(self,height):
        self.__height = height

    def get_area(self):  
        return self.__width * self.__height

    def get_perimeter(self):
        return 2 * (self.__width + self.__height)

    def get_diagonal(self):
        return math.sqrt(self.__width ** 2 + self.__height ** 2) 

    def get_picture (self):
        if self.__width > 50 or self.__height >50:
            return ("Too big for picture.") 
        return ("*" * self.__width + "\n") * self.__height

    def get_amount_inside(self, other):
        horizontal_fit = self.__width // other._Rectangle__width
        vertical_fit = self.__height // other._Rectangle__height
        
        return horizontal_fit * vertical_fit

    def __str__(self):
        return f"Rectangle(width={self.__width}, height={self.__height})"

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def set_width(self, side):
        super().set_width(side)

    def set_height(self, side):
        super().set_height(side)

    def set_side(self, side):
        super().set_width(side)
        super().set_height(side)

    def __str__(self):
        return f"Square(side={self._Rectangle__width})"

    

