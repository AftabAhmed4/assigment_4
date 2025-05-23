def get_user_numbers():
    user_numbers = []
    while True:
        user_input = input("Enter a number or leave blank to stop: ")
        
        # If the user enters a blank line, break out of the loop and stop asking for input
        if user_input == "":
            break
        
        # convert the user input to an integer and add it to the list
        num = int(user_input)
        user_numbers.append(num)
    
    return user_numbers

def count_nums(num_lst):
    num_dict = {}
    for num in num_lst:
        if num not in num_dict:
            num_dict[num] = 1
        else:
            num_dict[num] += 1
    
    return num_dict


def print_counts(num_dict):
    for num in num_dict:
        print(f"{num} appears {num_dict[num]} times.")


def show_dis_result_main():
    user_numbers = get_user_numbers()
    num_dict = count_nums(user_numbers)
    print_counts(num_dict)







# In this program we show an example of using dictionaries to keep track of information in a phonebook.
def read_phone_numbers():
    phonebook = {}
    while True:
        name = input("Enter Name or remains blank to empty: ")
        if name == '':
            break
        number = input("Number: ")
        phonebook[name] = number

    return phonebook

def print_phone_book(phonebook):
    for name in phonebook:
        print(f"{name}: {phonebook[name]}")


def search_in_phone_book(phonebook):
    while True:
        name = input("Write Name to Search: ")
        if name == '':
            break
        if name not in phonebook:
            print(f"{name} is not in phonebook")
        else:
            print(phonebook[name])
        
def phonebook_main():
    phonebook = read_phone_numbers()
    print_phone_book(phonebook)
    search_in_phone_book(phonebook)








# There's a small fruit shop nearby your house that you like to buy from. Since you buy several fruit at a time, you want to keep track of how much the fruit will cost before you go. Luckily you wrote down what fruits were available and how much one of each fruit costs.

def fruit_bill_main():

    fruits = {
        'apple': 10,
        'durian': 25,
        'jackfruit': 20.5,
        'kiwi': 12,
        'rambutan': 7,
        'mango': 8
    }

    total_cost = 0
    for fruit_name in fruits:
        price = fruits[fruit_name]
        purchase_quantity = int(input(f"How many {fruit_name} you want to purchase? "))
        total_cost += price * purchase_quantity
    print(f"Your total is ${total_cost}")










# You want to be safe online and use different passwords for different websites. However, you are forgetful at times and want to make a program that can match which password belongs to which website without storing the actual password!
from hashlib import sha256

def hashed_password(password):
    return sha256(password.encode()).hexdigest()


stored_logins = {
    "user1@example.com": hashed_password("mypassword123"),
    "user2@example.com": hashed_password("abcDEF456"),
}

def login(email, password_to_check):
    if email not in stored_logins:
        return False
    return hashed_password(password_to_check) == stored_logins[email]


def login_main():
    print(login("user1@example.com", "mypassword123"))
    print(login("user2@example.com", "abcDEF456")) 
    print(login("not_registered@example.com", "any")) 











# Python boilerplate.
if __name__ == '__main__':
    show_dis_result_main()
    phonebook_main()
    fruit_bill_main()
    login_main()