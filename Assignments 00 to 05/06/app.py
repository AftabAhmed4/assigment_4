# Write a function that takes two numbers and finds the average between the two.
def averge_num(num1, num2):
  return (num1 + num2 ) / 2
def averge_main():
  num1 = int(input("Enter the first number: "))
  num2 = int(input("Enter the second number: "))
  averge_num(num1, num2)
  print(f"The averge of the three numbers is: {averge_num(num1, num2)}")








# Fill out the chaotic_counting() function, which prints the numbers from 1 to 10, but with a catch. We've written a done() function which returns True with likelihood DONE_LIKELIHOOD -- at each number, before printing the number, you
import random

def chaotic_counting():
  for i in range(1, 11):
    if done():
      return
    print(f"num: {i}")


DONE_LIKELIHOOD = 0.3

def done():
  return random.random() < DONE_LIKELIHOOD

def chaotic_main():
  print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
  chaotic_counting()
  print("I am done!")









# Fill out the function count_even(lst) which
def generate_lst():
  user_input = input("Enter a number or press enter to stop: ")
  lst = []
  while user_input != '':
    lst.append(user_input)
    user_input = input("Enter a number or press enter to stop: ")
  return lst

def even_num(lst):
  for num in lst:
    if int(num) % 2 == 0:
      print(num)


def even_num_main():
  print("This program prints out even numbers.")
  lst = generate_lst()
  even_num(lst)








# Fill out the double(num) function to return the result of multiplying num by 2. We've written a main() function for you which asks the user for a number, calls your code for double(num) , and prints the result.
def double(num):
  return num * 2

def double_main():
  number = int(input("Enter a number: "))
  print(double(number))










# Fill out the get_name() function to return your name as a string! We've written a main() function for you which calls your function to retrieve your name and then prints it in a greeting.
def get_name():
    return "Smith"

def get_name_main():
    name = get_name()
    print(f"Steve {name}!")








# 0 even 11 odd 12 even 13 odd 14 even 15 odd 16 even 17 odd 18 even 19 odd
def is_odd(num):
  if num % 2 == 0:
    print(f"Even {num}")
  else:
    print(f"Odd {num}")

def is_odd_main():
  for i in range(12):
    is_odd(i)









# Write the helper function print_divisors(num), which takes in a number and prints all of its divisors (all the numbers from 1 to num inclusive that num can be cleanly divided by (there is no remainder to the division). Don't forget to call your function in main()!
def divisor(num):
  print("Here are the divisors of", num)
  for i in range(num):
    num_divisor = i+1
    if num % num_divisor == 0:
      print(num_divisor)

def divisor_main():
  num = int(input("Enter a number: "))
  divisor(num)










# Fill out print_multiple(message, repeats), which takes as parameters a string message to print, and an integer repeats number of times to print message. We've written the main() function for you, which prompts the user for a message and a number of repeats.
def message_display(message, times):
  for i in range(times):
    print(message)

def message_main():
  message_display("Hello World", 6)










# Implement the helper function make_sentence(word, part_of_speech) which will take a string word and an integer part_of_speech as parameters and, depending on the part of speech, place the word into one of three sentence templates (or one from your imagination!):
def make_sentence(word, part_of_speech):
  if part_of_speech == 0:
    print(f"I am excited to add this {word} to my vast collection of them!")  # noun
  elif part_of_speech == 1:
    print(f"It's so nice outside today it makes me want to {word}!") #verb
  elif part_of_speech == 2:
    print(f"Looking out my window, the sky is big and {word}!")
  else:
    print("Part of speech must be 0, 1, or 2! Can't make a sentence.")

def sentence_main():
  word: str = input("Enter a Word: ")
  print("Is this a noun, verb, or adjective?")
  part_of_speech: int = int(input("Type 0 for noun, 1 for verb, 2 for adjective: "))
  make_sentence(word, part_of_speech)











# Write a function called print_ones_digit , which takes as a parameter an integer num and prints its ones digit. The modulo (remainder) operator, %, should be helpful to you here. Call your function from main()!
def print_ones_digit(num):
  ones_digit = num % 10
  print(f"The ones digit is {ones_digit}")

def one_digit_main():
  number = int(input("Enter a number: "))
  print_ones_digit(number)











if __name__ == '__main__':
  averge_main()
  chaotic_main()
  even_num_main()
  double_main()
  get_name_main()
  is_odd_main()
  divisor_main()
  message_main()
  sentence_main()
  one_digit_main()