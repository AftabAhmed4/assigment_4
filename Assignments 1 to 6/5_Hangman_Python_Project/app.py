import random
import string

# List of possible words
word_list = ["apple", "banana", "grapes", "mango", "orange", "peach", "cherry"]

# Choose a random word
word = random.choice(word_list)
word_letters = set(word)  # Letters in the word
guessed_letters = set()   # Letters guessed by the player
alphabet = set(string.ascii_lowercase)  # All lowercase letters
lives = 6  # Total lives

print("Welcome to Hangman!")
print("Guess the word letter by letter.")
print(f"You have {lives} lives.\n")

# Game loop
while len(word_letters) > 0 and lives > 0:
    # Show current guessed word
    word_display = [letter if letter in guessed_letters else "_" for letter in word]
    print("Current word: ", " ".join(word_display))

    guess = input("Guess a letter: ").lower()

    # Check if input is valid
    if guess in alphabet - guessed_letters:
        guessed_letters.add(guess)

        if guess in word_letters:
            word_letters.remove(guess)
            print("Good job! Correct letter.\n")
        else:
            lives -= 1
            print(f"Wrong letter. You have {lives} lives left.\n")

    elif guess in guessed_letters:
        print("You already guessed that letter. Try again.\n")
    else:
        print("Invalid input. Please enter a letter.\n")

# Game result
if lives == 0:
    print(f"Game over! The word was: {word}")
else:
    print(f"Congratulations! You guessed the word: {word}")
