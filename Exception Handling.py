#Author: Eury T. Azucena
#Python Exception Handling

class Temperature:
    def __init__(self, celsius = 0, fahrenheit = 0):
        self.celsius = celsius
        self.fahrenheit = fahrenheit

class CelsiusToFahrenheit(Temperature):
    def __init__(self, celsius = 0):
        super().__init__(celsius)

    def CelToFar(self):
        Celsius = self.celsius
        fahrenheit = ((9/5)*Celsius)+32
        print("The Conversion Value to Fahrenheit is:",'%.2f'%fahrenheit,'°F')

class FahrenheitToCelsius(Temperature):
    def __init__(self, fahrenheit = 0):
        super().__init__(fahrenheit)

    def FahrToCels(self):
        Fahrenheit = self.fahrenheit
        celsius = (5/9)*(Fahrenheit-32)
        print("The Conversion Value to Celsius is:",'%.2f'%celsius,'°C')
    
class FahrenheitToKelvin(Temperature):
    def __init__(self, farenheit = 0):
        super().__init__(farenheit)

    def FahrToKel(self):
        Fahrenheit = self.fahrenheit
        Kelvin = (Fahrenheit + 459.67) * 5/9
        print("The Conversion Value to Kelvin is:",'%.2f'%Kelvin,'K')

class CelsiusToKelvin(Temperature):
    def __init__(self, celsius = 0):
        super().__init__(celsius)

    def CelToKel(self):
        Celsius = self.celsius
        Kelvin = Celsius + 273
        print("The Conversion Value to Kelvin is:",'%.2f'%Kelvin,'K')


# Main code
x = 1
while (x!=0):
    try:
        print("\nChoices \n 1 - Convert Temp from Celsius (C) to Fahrenheit (F) \n 2 - Convert Temp from Fahrenheit (F) to Celsius (C)  \n 3 - Convert Temp from Fahrenheit (F) to Kelvin (K) \n 4 - Conver Temp from Celsius (C) to Kelvin (K) \n 0 - Exit ") 
        Choices = int(input("Enter Choice: ")) 
    except:
        print("\n============================================")
        print("Error")
        print("============================================\n")
    finally:
        print("============================================")
        print("Enter the corresponds number only Exiting.....")
        print("============================================")
    if (Choices == 1):
        try:
            Celc = CelsiusToFahrenheit()
            Celc.celsius = float(input("\nEnter Temperature in Celsius(C): "))
            print("============================================")
            Celc.CelToFar()
            print("============================================")
        except:
            print("============================================")
            print("Please Enter a Numeral Numbers only Please")
            print("============================================")
        finally:
            print("\nConversion Program End")
            print("============================================")
        
    elif (Choices == 2):
        try:
            Fahr = FahrenheitToCelsius()
            Fahr.fahrenheit = float(input("\nEnter Temperature in Fahrenheit(F): "))
            print("============================================")
            Fahr.FahrToCels()
            print("============================================")
        except:
            print("============================================")
            print("Please Enter a Numeral Numbers only Please")
            print("============================================")
        finally:
            print("\nConversion Program End")
            print("============================================")
    elif (Choices == 3):
        try:
            Fahr2 = FahrenheitToKelvin()
            Fahr2.fahrenheit = float(input("\nEnter Temperature in Fahrenheit(F): "))
            print("============================================")
            Fahr2.FahrToKel()
            print("============================================")
        except:
            print("Please Enter a Numeral Numbers only Please")
        finally:
            print("\nConversion Program End")
            print("============================================")
    elif (Choices == 4):
        try:
            Celc2 = CelsiusToKelvin()
            Celc2.celsius = float(input("\nEnter Temperature in Celsius(C): "))
            print("============================================")
            Celc2.CelToKel()
            print("============================================")
        except:
            print("============================================")
            print("Please Enter a Numeral Numbers only Please")
            print("============================================")
        finally:
            print("\nConversion Program End")
            print("============================================")
    elif (Choices == 0):
        exit() 
    else: 
        print ("Invalid Input") 
