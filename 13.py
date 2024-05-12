class shape():
    def area(self):
        raise NotImplementedError
    def display(self):
        raise NotImplementedError

class circle(shape):
    def __init__(self, radius):
        self.radius = radius
        self.area_circle = 0
    def area(self):
        self.area_circle = 3.142 * self.radius * self.radius
    def display(self):
        print("area of the circle is: ",self.area_circle)
    
class triangle(shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
        self.area_triangle = 0
    def area(self):
        self.area_triangle = 1.5 * self.base * self.height
    def display(self):
        print("area of the rectangle is: ",self.area_triangle)

class rectangle(shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.area_rectangle = 0
    def area(self):
        self.area_rectangle = self.width * self.height
    def display(self):
        print("area of the circle is: ",self.area_rectangle)

Radius = int(input("enter radius"))
Height = int(input("enter height"))
Breadth = int(input("enter base"))
Length = int(input("enter length"))
Width = int(input("enter width"))

cir_obj = circle(Radius) 
cir_obj.area()
cir_obj.display()

tri_obj = triangle(Height,Breadth) 
tri_obj.area()
tri_obj.display()

rect_obj = rectangle(Length,Width) 
rect_obj.area()
rect_obj.display()

