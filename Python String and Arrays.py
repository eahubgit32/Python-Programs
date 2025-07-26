#Author: Eury T. Azucena
#Date: 11/16/2022
#Title: Python String and Arrays

#Display
import numbers
import string
import re


print ("====================================================================================================")
print ("                               University of San Agustin           ")
print ("                            Computer Engineering Department")
print ("Name: Eury T. Azucena                                     Filename: AzucenaCpE211L5" )
print ("Course Title: CpE2/CpE211- Object-Oriented Programming    Laboratory	  Date: November 16, 2022")
print ("Lab#5: Python String and Arrays")
print ("====================================================================================================\n")


class Check :

    # Constructor
    def __init__(self,word) :
        self.words = word

    def isPalindrome(self,word) :
        string = word
        rev_string = string[::-1]
        string = rev_string

        if self.words == string :
            print(self.words,"word is Palindrome")
        else :
            print(self.words,"word is not Palindrome")
    
class OppositeCase:
    def __init__(self, ch):
        self.words = ch

    def itsOppositeCase(self,ch):
        str = ch
        x=""
        for i in str:
            if(i.isupper()):
                x+=i.lower()
            else:
                x+=i.upper()
        print(x)


class PasswordGuess:
    def __init__(self,count):
        self.pw = count

    def main(self,count):
        while count < 3:
            password = input('Enter password: ')
            if password=='Eury':
                print('Access granted')
                break
            else:
                print('Access denied. Try again.')
                count += 1
                

class Arrays:
    def __init__(self, add):
        self.add = add

    
    def AddRemoveSort(self, add):
        print ("Previous List: ", Integer)
        Integer.append(add)
        print ("Updated List: ", Integer)

        print ("\n==Removing Integer==")
        remove = int(input("Remove integer: "))
        Integer.remove(remove)
        print ("Updated List:", Integer)

        print ("\n==Sorted Integer==")
        Integer.sort()
        print ("Updated List:", Integer)



# Main code 
x = 1 
while (x!=0):
    print("\nChoices \n 1 - Palindrome Program \n 2 - Opposite Case  \n 3 - Password Guess \n 4 - Add, delete, and sort elements from integer array \n 0 - Exit ") 
    Choices = int(input("Enter Choice: ")) 
    if (Choices == 1): 
        word = input("Enter a word: ")
        check_Palindrome = Check(word)
        check_Palindrome.isPalindrome(word)
    elif (Choices == 2):
        ch = input("Enter a word:")
        check_OppositeCase= OppositeCase(ch)
        check_OppositeCase.itsOppositeCase(ch)
    elif (Choices == 3):
        print('Enter correct password to continue')
        count = 0
        passwordguess = PasswordGuess(count)
        passwordguess.main(count)
    elif (Choices == 4):
        Integer = [2,3,5,11,4,6,8]
        print ("Current Integer List:", Integer)
        print ("\n==Adding Integer==")
        add = int(input("Add integer: "))
        adding = Arrays(add)
        adding.AddRemoveSort(add)
    elif (Choices == 0): 
        exit() 
    else: 
        print ("Invalid Input") 