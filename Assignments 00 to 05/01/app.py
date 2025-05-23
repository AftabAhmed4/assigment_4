import random 
#Simulate rolling two dice, three times. Prints the results of each die roll. This program is used to show how variable scope works.

def rolling_dice():
    print("This program roll two dice three times")
    i = 0
    while i < 3:
        max_number = 6
        dice_1 = random.randint(1, max_number)
        dice_2 = random.randint(1, max_number)
        print(f"Total of dice one {dice_1} and dice two {dice_2} is: {dice_1 + dice_2}")
        i += 1
    print("Dice rolled three times")


#Write a program that continually reads in mass from the user and then outputs the equivalent energy using Einstein's mass-energy equivalence formula (E stands for energy, m stands for mass, and C is the speed of light:

def mass_energy():
    C = 299792458
    user_input = int(input("Enter Mass in ( kg ): "))
    print("e = m * C^2...")
    print(f"m = {user_input} kg")
    print(f"C = {C} m/s")
    print(f"e = {user_input * (C*C)} joules of energy!")

# Converts feet to inches. Feet is an American unit of measurement. There are 12 inches per foot. Foot is the singular, and feet is the plural.

def feets_to_inches():
    user_input = int(input("Enter Enter number of feet: "))
    print(f"There is {user_input * 12} inches in {user_input} feet")

# Write a program that asks the user for the lengths of the two perpendicular sides of a right triangle and outputs the length of the third side (the hypotenuse) using the Pythagorean theorem!

def length_of_triangle():
    side_AB = int(input('Enter Length of AB Side (P): '))
    side_AC = int(input("Enter Length of AC Side (B): "))
    print("Pythagorean Theorem \n H^2 = B^2 + P^2")
    print(f"The length of BC (H) = {side_AB**2 + side_AC ** 2}")

# Ask the user for two numbers, one at a time, and then print the result of dividing the first number by the second and also the remainder of the division.

def division():
    dividend = int(input("Please enter an integer to be divided: "))
    divisor = int(input("Please enter an integer to be divide by: "))
    print(f"The quotient is {dividend // divisor} and the reminder is {dividend % divisor}")

#Simulate rolling two dice, and prints results of each roll as well as the total.
def two_dice():
    print("This program roll two dice and give its sum")
    dice_1 = random.randint(1, 6)
    dice_2 = random.randint(1, 6)
    print(f"The Sum of Dice one: {dice_1} and Dice two: {dice_2} is {dice_1 + dice_2}")


# Use Python to calculate the number of seconds in a year, and tell the user what the result
def sec_in_year():
    days_in_year = 365
    hours_in_day = 24
    minutes_in_hour = 60
    seconds_in_minutes = 60

    print(f"There are {days_in_year * hours_in_day * minutes_in_hour * seconds_in_minutes} seconds in a year!")


# Write a program which prompts the user for an adjective, then a noun, then a verb, and then prints a fun sentence with those words!

def mad_libs():
    adjective = input("Please type an adjective and press enter: ")
    noun = input("Please type an noun and press enter: ")
    verb = input("Please type an verb and press enter: ")
    print(f"Code in Place is fun. I learned to program and used Python to make my {adjective} {noun} {verb}!")




if __name__ == '__main__':
    rolling_dice()
    mass_energy()
    feets_to_inches()
    length_of_triangle()
    division()
    two_dice()
    sec_in_year()
    mad_libs()