import math
class Point: # 2 D Point
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __str__(self):
        return "Point is X = "+str(self.x)+\
        " Y = " + str(self.y)
    @staticmethod
    def distance(p1,p2):
        dist = math.sqrt(((p1.x - p2.x)**2)+ ((p1.y - p2.y)**2))
        print("The distance is ",dist)
    def __add__(self,other):
            print("In dunder add")
            if isinstance(other,Point):
                new_x = self.x + other.x
                new_y = self.y + other.y
                new_point = Point(new_x, new_y)
                return new_point
            elif(isinstance (other , int)):
                new_x = self.x + other
                new_y = self.y + other 
                new_point = Point(new_x, new_y)

                    
                return new_point
    def __sub__(self,other):
        new_x = self.x-other.x
        new_y = self.y - other.y 
        new_point = (Point(new_x, new_y))
        return new_point

    def __mul__(self,other):
        new_x = self.x * other.x
        new_y = self.y * other.y 
        new_point = (Point(new_x, new_y))
        return new_point

    def __floordiv__(self,other):
        new_x = self.x //other.x
        new_y = self.y // other.y 
        new_point = (Point(new_x, new_y))
        return new_point


    def __truediv__(self,other):
        new_x = self.x/other.x
        new_y = self.y / other.y 
        new_point = (Point(new_x, new_y))
        return new_point

    def __radd__(self,other):
        print("In r add method ")
        if isinstance(other,int):
            new_x = self.x + other
            new_y = self.y + other
            new_point = Point(new_x, new_y)
            return new_point

p1 = Point(10,20)
p2 = Point(20,20)
print(p1)
print(p2)
Point.distance(p1,p2)
print("Addition of two ",p1+p2) 
print("Difference of two  ",p1-p2)
print("Multiplication of two  ",p1 * p2 )
print("True division is ",p1/p2)
print("Floor division is ",p1//p2)
print(type(p1) is  Point) 
print("Reverse add is ",40 + p2)
