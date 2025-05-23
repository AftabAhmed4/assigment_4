# There are times where we want to return different things from a function based on some condition. To practice this idea, imagine that we want to check if someone is an adult. We might check their age and return different things depending on how old they are!
ADULT_AGE = 18

def is_adult():
  age = int(input("How old is this person?: "))
  if age >= ADULT_AGE:
    return True
  else:
    return False





# We've written a helper function for you called greet(name) which takes as input a string name and prints a greeting. Write some code in main() to get the user's name and then greet them, being sure to call the greet(name) helper function.
def greet_main():
  name = input("Enter Your Name: ")
  print(greet(name))

def greet(name):
  return f"Greeting {name}!"









# Implement the following function which takes in 3 integers as parameters:
def in_range(n, low, high):
  if n >= low and n <= high:
    return True
  else:
    return False













# Sophia has a fruit store. She has written a function num_in_stock which takes a string fruit as a parameter and returns how many of that fruit are in her inventory. Write code in main() which will:
def stock_main():
  fruit = input("Enter a fruit: ")
  stock = num_in_stock(fruit)
  if stock == 0:
    print("The Fruit is not in Stock")
  else:
    print(f"The Fruit is in Stock! Here is how many: {stock} ")

def num_in_stock(fruit):
  if fruit == "banana":
    return 50
  elif fruit == "apple":
    return 100
  elif fruit == "mango":
    return 18
  else:
    return 0










# There are times where you are working with lots of different data within a function that you want to return. While generally, we want to keep functions to have a precise purpose, sometimes that purpose just deals with multiple bits of data.
def user_data():
  first_name = input("Enter your first name: ")
  last_name = input("Enter your last name: ")
  email = input("Enter your email: ")
  return first_name, last_name, email

def data_main():
  data = user_data()
  print(f"Received the following user data: {data}")











# Fill out the subtract_seven helper function to subtract 7 from num, and fill out the main() method to call the subtract_seven helper function! If you're stuck, revisit the add_five example from lecture.
def subtract_seven(num):
  return num - 7

def subtract_main():
  num = int(input("Enter a number: "))
  result = subtract_seven(num)
  print(result)








if __name__ == '__main__':
    print(is_adult())
    greet_main()
    print(in_range(10, 5, 15))
    stock_main()
    data_main()
    subtract_main()