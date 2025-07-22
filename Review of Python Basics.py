#Author: Eury T. Azucena
#Date: 9/13/2022
#Title: Lab #1 Review of Basic Python


def Ch1():
    print("\n ====School Fees====")
    Misc= 8000
    Units = int(input("Enter total units enroll: "))
    dp = float(input("Enter Down payment: "))
    Tuition =  Units * 600.00
    Total_Fees = Tuition + Misc
    mp = (Total_Fees - dp) * 0.4
    fp = (Total_Fees - dp - mp)

    print("\n""Your payment for midterm: P",mp)
    print("Your payment for final: P",fp,"\n")
    print("====Break down Total Amount====")
    print("Cost per Unit: P600.00")
    print("Total enrolled units:",Units )
    print("Tuition: P",Tuition )
    print("Miscellaneous: P",Misc )
    print("Total school fees: P",Total_Fees,"\n" )


def Ch2():
    print("\n====Semester Weighted Average====")
    student = input("Student Name: ")
    program= input("Enter your program: ")
    L1=list()
    n = int(input("Numbers of courses enrolled: "))
    Sum=0
    for x in range(0,n):
        y=int(input("Enter Grade in percentage per course: "))
        L1.insert(x,y)
        Sum= Sum+L1[x]
        SWA= Sum/n
    print("\nSemester Weighted Average:", SWA)
    print("\nGrades per Course:", L1,"\n")
        


#Display
print ("============================================================================================")
print ("                               University of San Agustin           ")
print ("                            Computer Engineering Department")
print ("Name: Eury T. Azucena                                     Filename: AzucenaCpE211L1" )
print ("Course Title: CpE2/CpE211- Object-Oriented Programming    Laboratory	  Date: September 14, 2022")
print ("Lab#1: Review of Basic Python ")
print ("============================================================================================\n")  



#Main Program
x = 1 
while (x!=0): 
 print("Choices \n 1 - School Fees \n 2 - Semester Weighted Average \n 0 - Exit ") 
 Choices = int(input("Enter Choice:")) 
 if (Choices == 1) : 
   Ch1() 
 elif (Choices == 2) : 
   Ch2() 
 elif (Choices == 0): 
   exit() 
 else: 
   print ("Invalid Input") 