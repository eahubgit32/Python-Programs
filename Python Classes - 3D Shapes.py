#Author: Eury T. Azucena
#Date: 9/26/2022
#Title: Lab#3: Python Classes - 3D Shapes 

import math

#Class
class Cylinder:
    def __init__(self):
       self.height = float(input("Please Enter the Height of the Cylinder: "))
       self.radius = float(input("Please Enter the Radius of the Cylinder: "))
       Area = 2 * math.pi* self.radius * self.height
       Volume = math.pi*self.radius*self.radius
       print('\nVolume of Cylinder = %.2f' %Volume)
       print('Area of Cylinder = %.2f' %Area)


class Cone:
    def __init__(self):
        self.radius = float(input('Please Enter the Radius of a Cone: '))
        self.height = float(input('Please Enter the Height of a Cone: '))
        length = math.sqrt(self.radius * self.radius + self.height * self.height)
        SA = math.pi * self.radius * (self.radius + length)
        Volume = (1.0/3) * math.pi * self.radius * self.radius * self.height
        LSA = math.pi * self.radius  * length
        print("\nThe Surface Area of a Cone = %.2f " %SA)
        print("The Volume of a Cone = %.2f" %Volume)
        print("The Lateral Surface Area of a Cone = %.2f " %LSA)


class TPrism():
     def __init__(self):
        self.s1 = float(input("Enter Side 1 = "))
        self.s2 = float(input("Enter Side 2 = "))
        self.s3 = float(input("Enter Side 3 = "))
        self.length = float(input('Please Enter the Length of a Triangular Prism: '))
        self.base = float(input('Please Enter the Base of a Triangular Prism: '))
        self.height = float(input('Please Enter the Height of a Triangular Prism: '))
        SA = self.base * self.height + (self.s1 + self.s2 + self.s3) * self.length
        Volume = (self.length * self.base * self.height)/2
        print("\nThe Surface Area of a Triangular Prism = %.2f " %SA)
        print("The Volume of a Triangular Prism = %.2f" %Volume)


#Display
print ("====================================================================================================")
print ("                               University of San Agustin           ")
print ("                            Computer Engineering Department")
print ("Name: Eury T. Azucena                                     Filename: AzucenaCpE211L3" )
print ("Course Title: CpE2/CpE211- Object-Oriented Programming    Laboratory	  Date: September 26, 2022")
print ("Lab#3: Python Classes - 3D Shapes ")
print ("====================================================================================================\n") 
 



#Main Program
x = 1 
while (x!=0): 
 print("Choices \n 1 - Compute Area and Volume of Cylinder \n 2 - Compute Area and Volume of Cone \n 3 - Compute Area and Volume of Prism \n 0 - Exit") 
 Choices = int(input("Enter Choice: ")) 
 if (Choices == 1): 
    print("\n===Area and Volume of Cylinder===\n")
    Cylinder()
 elif (Choices == 2):
    print("\n===Area and Volume of Cone===\n")
    Cone()
 elif (Choices == 3):
    print("\n===Area and Volume of Prism===\n")
    TPrism()
 elif (Choices == 0):
    exit()
 else:
    print("Invalid Input")