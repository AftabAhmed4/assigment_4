# Guess My Number
import random

def guess_main():
  secret_num = random.randint(1, 99)
  guess = int(input("Guess a number between 1 and 99: "))

  while guess != secret_num:
    if guess < secret_num:
      print("Too low!")
    else:
      print("Too high!")
    guess = int(input("Guess again: "))
  print("You got it!")








# Write a program to print terms in the Fibonacci sequence up to a maximum value.
MAX = 10000

def fibonacci_main():
  a = 0
  b = 1

  while a < MAX:
    print(a, end=" ")
    next_num = a + b
    a = b
    b = next_num










# Write a program that prints the first 20 even numbers. There are several correct approaches, but they all use a loop of some sort. Do no write twenty print statements
def even_main():
  for i in range(20):
    print(i * 2)









# Write a program which prompts the user to type an affirmation of your choice (we'll use "I am capable of doing anything I put my mind to.") until they type it correctly. Sometimes, especially in the midst of such uncertain times, we just need to be reminded that we are resilient, capable, and strong; this little Python program may be able to help!
Affirmation = "I am capable of doing anything I put my mind to."

def affirmation_main():
  print(f"Please type the following affirmation: {Affirmation}")

  user_input = input()

  while user_input != Affirmation:
    print("That was not the affirmation.")

    print(f"Please type the following affirmation: {Affirmation}")
    user_input = input()

  print("That was the affirmation!")








# Write a program that prints out the calls for a spaceship that is about to launch. Countdown from 10 to 1 and then output Liftoff!
def liftover_main():
  for i in range(10):
    print(10 - i, end=" ")
  print("Liftover!")








# Write a program that asks a user to enter a number. Your program will then double that number and print out the result. It will repeat that process until the value is 100 or greater.
def double_main():
  curr_value = int(input("Enter Number to double: "))
  while curr_value < 100:
    curr_value = curr_value * 2
    print(curr_value, end=' ')







if __name__ == '__main__':
  guess_main()
  fibonacci_main()
  even_main()
  affirmation_main()
  liftover_main()
  double_main()