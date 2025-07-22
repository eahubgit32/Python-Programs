#Author: Eury T. Azucena
#Date: 9/21/2022
#Title: Lab #2 UML Diagrams


import math

class Square:
    def areaOfSquare(self, s):
        return s*s


class poly:
    def __init__(self, a, b, c):
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)
        self.area = 0

class triangle(poly):
    def __init__(self, a, b, c):
        poly.__init__(self, a, b, c)

    def calculate_area(self):
        s = (self.a + self.b + self.c) / 2
        self.area = float((s * (s - self.a) * (s - self.b) * (s - self.c))) ** 0.5

    def get_area(self):
        return self.area     



class Circle:
    Pi = 3.142
    def __init__(self,radius):
       self.radius = radius
    def area(self):
       return(Circle.Pi*self.radius*self.radius)


#Display
print ("====================================================================================================")
print ("                               University of San Agustin           ")
print ("                            Computer Engineering Department")
print ("Name: Eury T. Azucena                                     Filename: AzucenaCpE211L1" )
print ("Course Title: CpE2/CpE211- Object-Oriented Programming    Laboratory	  Date: September 21, 2022")
print ("Lab#2: UML Diagrams ")
print ("====================================================================================================\n") 
 

x = 1 
while (x!=0): 
 print("Choices \n 1 - Compute Area of Square \n 2 - Compute Area of Triangle \n 3 - Compute Area of Circle \n 0 - Exit") 
 Choices = int(input("Enter Choice: ")) 
 if (Choices == 1): 
    print ("\n==Computing Area of Square==",'\n')
    print("Enter the Side Length of Square: ", end="")
    l = float(input())
    obj = Square()
    a = obj.areaOfSquare(l)
    print("\nArea of Square = {:.2f}".format(a),'\n')
 elif (Choices == 2): 
    print ("\n==Computing Area of Triangle==",'\n')
    a, b, c = input("Left Side = "), input("Right Side = "), input("Base = ")
    t = triangle(a, b, c)
    t.calculate_area()
    print("\nArea of Triangle = {:.2f}".format(t.get_area()),'\n')
 elif (Choices == 3):
    print ("\n==Computing Area of Circle==",'\n')
    rad = int(input("Enter Radius: "))
    c1 = Circle(rad) 
    print("\nArea of Circle = ", c1.area(),'\n') 
 elif (Choices == 0): 
   exit() 
 else: 
   print ("Invalid Input") 