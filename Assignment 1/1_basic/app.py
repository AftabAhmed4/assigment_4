# Write a simple joke bot. The bot starts by asking the user what they want. However, your program will only respond to one response: Joke.

PROMPT: str = "What do you want? "
JOKE: str = "Here is a joke for you! Panaversity GPT - Sophia is heading out to the grocery store. A programmer tells her: get a liter of milk, and if they have eggs, get 12. Sophia returns with 13 liters of milk. The programmer asks why and Sophia replies: 'because they had eggs'"
SORRY: str = "Sorry! i tell joke only."

def joke_main():
    user_input = input(PROMPT).strip().lower()

    if "joke" in user_input:
        print(JOKE)
    else:
        print(SORRY)







# Write a program that asks a user to enter a number. Your program will then double that number and print out the result. It will repeat that process until the value is 100 or greater.

def double_main():
    curr_value = int(input("Enter a number: "))

    while curr_value < 100:
        curr_value * 2
        curr_value = curr_value * 2
        print(curr_value)






# Write a program that prints out the calls for a spaceship that is about to launch. Countdown from 10 to 1 and then output Liftoff!

def liftover_main():
    for i in range(10, 0, -1):
        print(i, end=' ')
    print("Liftover!")









# Guess My Number
import random

def guess_number_main():
    secret_number = random.randint(1, 99)
    print("Guess Number Between 1 to 100")
    user_input = int(input("Enter Number (1 to 100): "))
    while user_input != secret_number:
        if user_input < secret_number:
            print("Guess Too Low!")
        else:
            print("Guess Too High!")

        user_input = int(input("Enter Number (1 to 100): "))
    print(f"Congrats! The number was: {secret_number}")








# Print 10 random numbers in the range 1 to 100.

def random_main():
    for _ in range(10):
        value = random.randint(1, 100)
        print(value, end=" ")









if __name__ == '__main__':
    # joke_main()
    # double_main()
    # liftover_main()
    # guess_number_main()
    random_main()