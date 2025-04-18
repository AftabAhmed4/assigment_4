# Write a Python program that takes two integer inputs from the user and calculates their sum. The program should perform the following tasks:

def sum ():
    print("This program add two number \n" )
    num_1 = int(input("Enter number 1: "))
    num_2 =int(input("Enter number 2: "))
    print( num_1+num_2)

# Write a program which asks the user what their favorite animal is, and then always responds with "My favorite animal is also ___!" (the blank should be filled in with the user-inputted animal, of course).

def favorite_animals ():
    print("This program takes favorite animal name \n" )
    favorite = input("Enter your favorite animal name: ")
    print(f"My favorite animal is also {favorite}!")


# Write a program which prompts the user for a temperature in Fahrenheit (this can be a number with decimal places!) and outputs the temperature converted to Celsius.

def fah_to_temp ():
    print("this program convert fahrenhit to celsius \n" )
    Fahrenheit = int(input("Enter temperature in Fahrenheit: "))
    print(f"Temperature: {Fahrenheit}F = {(Fahrenheit - 32) * 5.0/9.0}C")

# Write a program to solve this age-related riddle!
def age_problem():
    print("this program solve age problem \n" )
    anton = 21
    beth = anton + 6
    chen = beth + 20
    drew = chen + anton
    ethan = chen

    print("Anton is " + str(anton))
    print("Beth is " + str(beth))
    print("Chen is " + str(chen))
    print("Drew is " + str(drew))
    print("Ethan is " + str(ethan))

# Prompt the user to enter the lengths of each side of a triangle and then calculate and print the perimeter of the triangle (the sum of all of the side lengths).

def  perimeter():
    print("this program find the perimeter of the triangle  \n" )
    side_1 = float(input("What is the length of side 1? "))
    side_2 = float(input("What is the length of side 2? "))
    side_3 = float(input("What is the length of side 3? "))
    print(f"The perimeter of the triangle is {side_1+ side_2+side_3}")

# Ask the user for a number and print its square (the product of the number times itself).
def square ():
    user_input =int(input("Type a number to see its square: "))
    print(f"{user_input} squared is {user_input**2}")





if __name__ == '__main__':
    sum()
    favorite_animals()
    fah_to_temp()
    age_problem()
    perimeter()
    square()
