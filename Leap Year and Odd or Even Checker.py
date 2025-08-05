# Eury T. Azucena
# Leap Year and Odd or Even Checker

def is_leap_year(year):
    """Returns True if the year is a leap year, else False."""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def odd_or_even(number):
    """Returns 'Odd' if the number is odd, 'Even' if it's even."""
    return "Odd" if number % 2 != 0 else "Even"

# Get user input
year = int(input("Enter a year: "))
number = int(input("Enter a number: "))

# Display results
print(f"{year} is a leap year: {is_leap_year(year)}")
print(f"{number} is {odd_or_even(number)}")