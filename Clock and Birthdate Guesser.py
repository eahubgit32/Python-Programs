#Author: Eury T. Azucena
#Date: 12/16/2022
#Title: Clock and Birthdate Guesser

from tkinter import *
from time import*
from datetime import date

#Display
print ("====================================================================================================")
print ("                               University of San Agustin           ")
print ("                            Computer Engineering Department")
print ("Name: Eury T. Azucena                                     Filename: AzucenaCpE211L8" )
print ("Course Title: CpE2/CpE211- Object-Oriented Programming    Laboratory	  Date: December 16, 2022")
print ("Title: Birthday and Age Problem, Digital Clock")
print ("====================================================================================================\n")


def CalAge(current_date, current_month, current_year,
            birth_date, birth_month, birth_year):
 
     
    month =[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (birth_date > current_date):
        current_month = current_month - 1
        current_date = current_date + month[birth_month-1]
         
         
    if (birth_month > current_month):        
        current_year = current_year - 1;
        current_month = current_month + 12;
         

    calculated_date = current_date - birth_date;
    calculated_month = current_month - birth_month;
    calculated_year = current_year - birth_year;
     
    
    print("\n================================================")
    print("Present Age")
    print("Age:", calculated_year, "Month\s:", 
         calculated_month, "Day\s:", calculated_date)
    print("================================================")

def Birthday():
    today  = date.today()
    current_date = today.day
    current_month = today.month
    print("\n================================================")
    year = int(input('Enter Age: '))
    Month = int(input('Enter Number of Months [MM]: '))
    Date = int(input('Enter Number of Day/s [DD]: '))
    print("================================================\n")

    month =[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (Date > current_date):
        current_month = current_month - 1
        current_date = current_date + month[Month-1]

    if (Month > current_month):        
        current_month = current_month + 12;
    
    calculated_date = current_date - Date;
    calculated_month = current_month - Month;
    Years = today.year - year

    print("\n================================================")
    print("Birthdate")
    print("Year:",Years,  "Month\s:", calculated_month, "Day\s:", calculated_date)
    print("================================================")


def clock():
    time_string = strftime("%I:%M:%S %p")
    time_label.config(text=time_string)

    day_string = strftime("%A")
    day_label.config(text=day_string)

    date_string = strftime("%B %d, %Y")
    date_label.config(text=date_string)

    window.after(1000,clock)

# Main code
x = 1
while (x!=0):
    print("\nChoices \n 1 - Age Calculator \n 2 - Birthday Calculator  \n 3 - Digital Clock  \n 0 - Exit ") 
    Choices = int(input("Enter Choice: ")) 
    if (Choices == 1):
        today = date.today()
        current_date = today.day
        current_month = today.month
        current_year = today.year
         
        birth_year = int(input('Enter Birth Year [YYYY]: '))
        birth_month = int(input('Enter Birth Month [MM]: '))
        birth_date = int(input('Enter Birth Day [DD]: '))
 
        CalAge(current_date, current_month, current_year,
                birth_date, birth_month, birth_year)
        
    elif (Choices == 2):
       Birthday()
            
    elif (Choices == 3):
        window = Tk()
        window.title("Eury's Digital Clock")
        time_label = Label(window,font=("Arial",50),fg="#00FF00",bg="black")
        time_label.pack()

        day_label = Label(window,font=("Arial",25,"bold"))
        day_label.pack()

        date_label = Label(window,font=("Arial",30))
        date_label.pack()
        clock()

        window.mainloop()
           
    elif (Choices == 0):
        exit() 
    else: 
        print ("Invalid Input") 