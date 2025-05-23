def even_number ():
    for num in range(21):
        print (num *2 )

# Write a program which asks a user for their age and lets them know if they can or can't vote in the following three fictional countries.


indonesia = 17
united_states = 18
malaysia = 21

def vote_eligible():
    user_input = int(input("How old are you? "))

    if user_input >= malaysia:
        print(f"You can vote in all listed countries (Indonesia, United States, Malaysia).")

    elif user_input >= united_states:
        print(f"You can vote in Indonesia and the United States.")
        print(f"You cannot vote in Malaysia where the age limit is {malaysia}.")

    elif user_input >= indonesia:
        print(f"You can vote in Indonesia.")
        print(f"You cannot vote in United States (age {united_states}) or Malaysia (age {malaysia}).")

    else:
        print(f"You cannot vote in any of the listed countries.")
        print(f"Indonesia voting age: {indonesia}")
        print(f"United States voting age: {united_states}")
        print(f"Malaysia voting age: {malaysia}")

# Write a program that reads a year from the user and tells whether a given year is a leap year or not
def is_leap_year(year):
    if (year % 4 == 0):
        if (year % 100 != 0) or (year % 400 == 0):
            return True
    return False

# Try with input
year = int(input("Enter a year: "))
if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")


# Write a program which asks the user how tall they are and prints whether or not they're taller than a pre-specified minimum height.

MINIMUM_HEIGHT = 50

def tall_enough_extension():
    height = int(input("How tall are you? "))
    if height >= MINIMUM_HEIGHT:
        print("You're tall enough to ride!")
    else:
        print("You're not tall enough to ride, but maybe next year!")


# Print 10 random numbers in the range 1 to 100.
import random
def random_number():
    number = 0
    for num in range (10):
        number = random.randint (1,100)
        print(f"{num + 1}: {number}")
























if __name__ == "__main__":
    even_number()
    vote_eligible()
    is_leap_year(year)
    tall_enough_extension()
    random_number()



