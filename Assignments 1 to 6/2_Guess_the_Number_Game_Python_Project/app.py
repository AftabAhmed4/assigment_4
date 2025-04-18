import random

def guess_the_number():
    print("Welcome to the 'Guess the Number' game!")
    print("I'm thinking of a number between 1 and 100.")

    # Computer chooses a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 6

    while attempts > 0:
        print(f"Avaliable Attempts {attempts}")
        try:
            user_guess = int(input("Take a guess: "))
            attempts -= 1

            if user_guess < number_to_guess:
                print("Too low! Try again.")
            elif user_guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"🎉 Congratulations! You guessed the number in {attempts} tries.")
                break
        except ValueError:
            print("Please enter a valid number.")

# Run the game
guess_the_number()
