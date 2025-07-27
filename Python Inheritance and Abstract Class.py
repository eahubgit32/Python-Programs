#Author: Eury T. Azucnea
#Date: 11/25/2022
#Title: Python Inheritance and Abstract Class


#Display
print ("====================================================================================================")
print ("                               University of San Agustin           ")
print ("                            Computer Engineering Department")
print ("Name: Eury T. Azucena                                     Filename: AzucenaCpE211L6" )
print ("Course Title: CpE2/CpE211- Object-Oriented Programming    Laboratory	  Date: November 25, 2022")
print ("Lab#6: Python Inheritance and Abstract Class")
print ("====================================================================================================\n")


#Class
class Person:
    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age

    def View(self):
        print("Name: ",self.fname,self.lname)
        print("Age: ",self.age)
    
    def Age(self):
        if self.age < 18:
            print('The customer is minor')
        else: 
            print('The customer is not minor')

class Customer(Person):
    def __init__(self, fname, lname, age, number,):
        super().__init__(fname, lname, age)
        self.number = number
    
    def show(self):
        print("Customer Number: ", self.number)



class Shape:
    def __init__(self):
        pass

    def getArea(self):
        pass
    
class Rectangle(Shape):
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def getArea(self):
        return self.length*self.width



class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def getArea(self):
        return 3.14*(self.radius**2)

    def getDiameter(self):
        return 2*self.radius


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def getArea(self):
        return 0.5*self.base*self.height


    
# Main code 
x = 1 
while (x!=0):
    print("\nChoices \n 1 - Person \n 2 - Shape \n 3 - File Handling \n 0 - Exit ") 
    Choices = int(input("Enter Choice: ")) 
    if (Choices == 1):
        print("\n======INPUT SCREEN========")
        customer = Customer(0, 0, 0, 0)
        customer.fname = (input("Enter First name: "))
        customer.lname = (input("Enter Last Name: "))
        customer.age = int(input("Enter Age: "))
        customer.number = (input("Enter Number: "))
        print("===========================")
        print("\n======OUTPUT SCREEN=======")
        customer.View()
        customer.show()
        customer.Age()
        print("===========================")
    elif (Choices == 2):
        print("\nSub-Choices \n a - Rectangle \n b - Circle \n c - Triangle")
        Choice = (input("Enter Choice: "))
        if (Choice == "a"):
            print("\n======INPUT SCREEN========")
            l=float(input("Enter length of rectangle: "))
            b=float(input("Enter Width of rectangle: "))
            obj=Rectangle(l,b)
            print("===========================")
            print("\n======OUTPUT SCREEN=======")
            print("Length of rectangle:", l, "\nWidth of rectangle:", b )
            print("Area of rectangle:",obj.getArea())
            print("===========================")
        elif (Choice == "b"):
            print("\n======INPUT SCREEN========")
            r = float(input("Enter Radius of Cirlce: "))
            obj = Circle(r)
            print("===========================")
            print("\n======OUTPUT SCREEN=======")
            print("Radius of Circle:", r)
            print("Area of Circle:", obj.getArea())
            print("Diameter of Circle:", obj.getDiameter())
            print("===========================")
        elif (Choice == "c"):
            print("\n======INPUT SCREEN========")
            b = float(input("Enter Base of Triangle: "))
            h = float(input("Enter Height of Triangle: "))
            obj = Triangle(b,h)
            print("===========================")
            print("\n======OUTPUT SCREEN=======")
            print("Base of Triangle:",b,"\nHeight of Triangle:", h)
            print("Area of Triangle:", obj.getArea())
            print("===========================")
    elif (Choices == 3):

        file = open("Student.txt", "r")
        print("============ TEXT FILE =============")
        print(file.read())
        print("===================================")
        file = open("Student.txt", "a")
        print("============ APPEND FILE =============")
        address = input("Enter Address: ")
        address = ("\nAddress: " +address)
        file.write(address)
        email = input("Enter USA Email: ")
        email = ("\nUSA Email: " +email)
        file.write(email)
        course = input("Enter Course & Year: ")
        course = ("\nCourse & Year: " +course)
        file.write(course)
        file.close()
    elif (Choices == 0):
        exit()
    else: 
        print ("Invalid Input") 