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


if __name__ == '__main__':
    rolling_dice()