# We want you to gain more experience working with control flow and Booleans in Python. To do this, we are going to have you develop a game! The game is called High-Low and the way it's played goes as follows:
import random 


def high_low_game():
    print("\nWelcome to the High-Low Game!")
    print("==============================")

    number = 0

    for i in range(4):

        computer_number = random.randint(1, 99)
        user_number = random.randint(1, 99)

        print(f"\nRound {i + 1}")

        print(f"Your Number is {user_number}")

        guess = input("Do you think your number is higher or lower than the computer's? ").strip().lower()

        high_and_correct = guess == 'higher' and user_number > computer_number
        low_and_correct = guess == 'lower' and user_number < computer_number

        if high_and_correct or low_and_correct:
            print(f"You were right! The computer's number was {computer_number}")
            number += 1
            print(f"Your score is now {number}")
        else:
            print(f"Aww, that's incorrect. The computer's number was {computer_number}")
            print(f"Your score is now {number}")

    print("\nThanks for playing!")














# Mars Weight Solution and planet weight solution
MERCURY_GRAVITY = 0.376
VENUS_GRAVITY = 0.889 
MARS_GRAVITY = 0.378
JUPITER_GRAVITY = 2.36 
SATURN_GRAVITY = 1.081
URANUS_GRAVITY = 0.815 
NEPTUNE_GRAVITY = 1.14 
EARTH_GRAVITY = 1.0

def weight_main():
    earth_weight = float(input("Enter weight in earth: "))
    planet = input("Enter a planet name: ").strip().lower()

    gravity_constant = ''

    if planet == 'mercury':
        gravity_constant = MERCURY_GRAVITY
    elif planet == 'venus':
        gravity_constant = VENUS_GRAVITY
    elif planet == 'mars':
        gravity_constant = MARS_GRAVITY
    elif planet == 'jupiter':
        gravity_constant = JUPITER_GRAVITY
    elif planet == 'saturn':
        gravity_constant = SATURN_GRAVITY
    elif planet == 'uranus':
        gravity_constant = URANUS_GRAVITY
    elif planet == 'neptune':
        gravity_constant = NEPTUNE_GRAVITY
    else:
        gravity_constant = EARTH_GRAVITY
        planet = "Earth"
    
    planetary_weight = earth_weight * gravity_constant
    rounded_weight = round(planetary_weight, 2)

    print(f"The equivalent weight on {planet.capitalize()} is {rounded_weight}")












# =================================== LIST AND DICTIONARY ==========================================
# Problem #1: List Practice 
fruit_list = ['apple', 'banana', 'orange', 'grape', 'pineapple']
print(len(fruit_list))
fruit_list.append('mango')
print(fruit_list)



# Problem #2: Index Game

def access_element(list, index):
    try:
        return f"Elemet at {index}: {list[index]}"
    except:
        return f"Elemet not found at {index}"


def modify_element(list, index, new_value):
    try:
        old_value = list[index]
        list[index] = new_value
        return f"Modified value from {old_value} to {new_value}"
    except:
        return f"Elemet not found at {index}"
    

def slice_list(list, start, end):
    try:
        return list[start: end]
    except Exception as e:
        return f"Error: {e}"




def list_main():
    my_list = ['apple', 'banana', 'cherry', 'date', 'elderberry']
    print("Welcome to the Index Game!")
    print("Current list:", my_list)

    while True:
        print("\nChoose an operation:")
        print("1. Access an element")
        print("2. Modify an element")
        print("3. Slice the list")
        print("4. Exit")
        choice = input("Enter your choice (1/2/3/4): ").strip()

        if choice == '1':
            try:
                index = int(input("Enter the index you want to access: "))
                result = access_element(my_list, index)
                print(result)
            except ValueError:
                print("Please enter a valid number.")
        
        elif choice == '2':
            try:
                index = int(input("Enter the index you want to modify: "))
                new_value = input("Enter the new value: ")
                result = modify_element(my_list, index, new_value)
                print(result)
                print("Updated list:", my_list)
            except ValueError:
                print("Please enter a valid number.")
        
        elif choice == '3':
            try:
                start = int(input("Enter the start index: "))
                end = int(input("Enter the end index: "))
                result = slice_list(my_list, start, end)
                print("Sliced list:", result)
            except ValueError:
                print("Please enter valid numbers.")

        elif choice == '4':
            print("Thanks for playing the Index Game!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")









if __name__ == "__main__":
    # high_low_game()
    # weight_main()
    list_main()