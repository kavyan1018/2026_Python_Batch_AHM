from abc import ABC, abstractmethod

class Shape(ABC):
    
    @abstractmethod
    def area(self):
        pass            # -> we are not providing an implementation for this method, so we are using pass    

class Circle(Shape):
    
    def __init__(self, radius):
        print("Circle constructor called")
        self.radius = radius
        
    def area(self):
        return 3.14 * self.radius * self.radius        


class Square(Shape):
    def __init__(self, side):
        print("Square constructor called")
        self.side = side
        
    def area(self):
        return self.side * self.side

s = Circle(5)


print("Area of Circle:", s.area())    
print("Area of Square:", Square(4).area())