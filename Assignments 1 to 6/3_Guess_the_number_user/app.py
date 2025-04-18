import random

def computer_guess():
    print("Think of a number between 1 and 100, and I will try to guess it!")
    print("After each guess, tell me if it's 'high', 'low', or 'correct'.")

    low = 1
    high = 100
    feedback = ''
    attempts = 0

    while feedback != 'correct':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # or high, both are same here

        attempts += 1
        print(f"My guess is: {guess}")
        feedback = input("Is it 'high', 'low', or 'correct'? ").lower()

        if feedback == 'high':
            high = guess - 1
        elif feedback == 'low':
            low = guess + 1
        elif feedback != 'correct':
            print("Please enter a valid response: 'high', 'low', or 'correct'.")

    print(f"🎉 Yay! I guessed your number in {attempts} tries!")

# Run the game
computer_guess()
