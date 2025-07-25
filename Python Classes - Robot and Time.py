#Author: Eury T. Azucena
#Date: 10/9/2022
#Title: Lab 4 Python Classes – Robot and Time

import datetime

#Display
print ("====================================================================================================")
print ("                               University of San Agustin           ")
print ("                            Computer Engineering Department")
print ("Name: Eury T. Azucena                                     Filename: AzucenaCpE211L4" )
print ("Course Title: CpE2/CpE211- Object-Oriented Programming    Laboratory	  Date: October 10, 2022")
print ("Lab#4: Python Classes – Robot and Time ")
print ("====================================================================================================\n")


class Robo:
    def __init__(self, name, made_date=None, Maker=None):
        self.name = name
        self.made_date = made_date
        self.Maker = Maker
    def set_name(self, name):
        self.name = name
    
    def get_name(self):
        return self.name 

    def madeDate (self, made_date):
        self.made_date = made_date
    
    def get_madeDate(self):
        return self.made_date
    
    def maker (self, Maker):
        self.Maker = Maker
    
    def get_maker(self):
        return self.Maker

    def greet(self):
        if self.name:
            print("Hi, I am " + self.name)
        else:
            print("Hi, I am a robot without a name")
        if self.made_date:
            print("I am Made at the time and day of: " + self.made_date)
        else:
            print("My made date is Unknown")
        if self.Maker:
            print("My maker is " + self.Maker)
        else:
            print("My maker is not known!")
    def actions(self, status):
        if (status == 1):
            print("\n=====================")
            print ("I am talking now")
            print("=====================\n")
        elif (status == 2): 
            print("\n=====================")
            print ("I am walking now")
            print("=====================\n")
        elif (status == 3):
            print("\n=====================")
            print ("I am dancing now")
            print("=====================\n")
        elif (status == 0): 
            exit() 
        else:
            print ("Invalid input")


x = 1 
while (x!=0):
    print("\n==============ROBOT INTERFACE====================")
    robo = Robo("Patrick","10/9/2022","Eury")
    robo.greet()
    print("\n==============ACTION SCREEN====================")
    print("1 - Talk \n2 - Walk \n3 - Dance \n0 - Exit")
    Status = int(input("Enter Action Choice: ")) 
    robo.actions(Status)
    now = datetime.datetime.now()
    print("=============================================")
    print("Current date and time: ", now.strftime("%Y-%m-%d %H:%M:%S"))
    print("=============================================\n")