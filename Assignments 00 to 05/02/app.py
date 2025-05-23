# Write a function that takes a list of numbers and returns the sum of those numbers.

def add_many_numbers ():
    number_list = [3,5,7,9,12,3,15,12,14,12,56]
    sum=0
    for num in number_list:
        sum += num
    print(f"This is sum of list: {sum}")


# Write a program that doubles each element in a list of numbers.

def double_list():
    numbers_list = [2, 4, 1, 6, 8]
    doubled_list = [num * 2 for num in numbers_list]
    print(doubled_list)


# Implement an 'eraser' on a canvas
# app.py

# graphics.py

from tkinter import *
class SimpleCanvas:
    def __init__(self, width, height):
        self.root = Tk()
        self.root.title("Canvas App")
        self.canvas = Canvas(self.root, width=width, height=height, bg="white")
        self.canvas.pack()
        self._click_pos = None
        self.root.update()

    def create_rectangle(self, x1, y1, x2, y2, color):
        return self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline='black')

    def moveto(self, obj, x, y):
        bbox = self.canvas.bbox(obj)
        if bbox:
            cur_x, cur_y = bbox[0], bbox[1]
            dx = x - cur_x
            dy = y - cur_y
            self.canvas.move(obj, dx, dy)
        self.root.update()

    def set_color(self, obj, color):
        self.canvas.itemconfig(obj, fill=color)
        self.root.update()

    def find_overlapping(self, x1, y1, x2, y2):
        return self.canvas.find_overlapping(x1, y1, x2, y2)

    def wait_for_click(self):
        self._click_pos = None
        self.canvas.bind("<Button-1>", self._on_click)
        while self._click_pos is None:
            self.root.update()
        self.canvas.unbind("<Button-1>")

    def get_last_click(self):
        return self._click_pos

    def get_mouse_x(self):
        return self.canvas.winfo_pointerx() - self.canvas.winfo_rootx()

    def get_mouse_y(self):
        return self.canvas.winfo_pointery() - self.canvas.winfo_rooty()

    def _on_click(self, event):
        self._click_pos = (event.x, event.y)




# fill out the add_three_copies(...) function which takes a list and some data and then adds three copies of the data to the list.

def add_three_copies ():
    user_input = input("Enter a string: ")
    user_list=[]
    for i in range(3):
        user_list.append(user_input)
    print(user_list)


# Fill out the function get_first_element(lst) which takes in a list lst as a parameter and prints the first element in the list.

def get_first_element(lst):
    print(f"The First Element of list is: {lst[0]}")

def generate_list_first():
    lst = []
    user_input = input("Please enter an element of the list or press enter to stop: ")
    while user_input != '':
        lst.append(user_input)
        user_input = input("Please enter an element of the list or press enter to stop: ")
    return lst

def first_element_list():
    lst = generate_list_first()
    get_first_element(lst)


# Fill out the function get_last_element(lst) which takes in a list lst as a parameter and prints the last element in the list.
def get_last_element(lst):
    print(f"The Last Element of list is: {lst[len(lst) - 1]}")

def generate_list_last():
    lst = []
    user_input = input("Please enter an element of the list or press enter to stop: ")
    while user_input != '':
        lst.append(user_input)
        user_input = input("Please enter an element of the list or press enter to stop: ")
    return lst

def last_element_list():
    lst = generate_list_last()
    get_last_element(lst)


# Write a program which continuously asks the user to enter values which are added one by one into a list. When the user presses enter without typing anything, print the list.

def generate_list():
    lst = []
    user_input = input("Please enter an element of the list or press enter to stop: ")   
    while  user_input != '':
        lst.append(user_input)
        user_input = input("Please enter an element of the list or press enter to stop: ")  
    return lst

def show_list():
    lst = generate_list()
    print(lst)


# Fill out the function shorten(lst) which removes elements from the end of lst, which is a list, and prints each item it removes until lst is MAX_LENGTH items long. 

def generate_lst():
    lst = []
    user_input = input("Please enter an element of the list or press enter to stop: ")
    while user_input != '':
        lst.append(user_input)
        user_input = input("Please enter an element of the list or press enter to stop: ")
    return lst

def show_generated_list():
    MAX_LENGTH = 3
    lst = generate_lst()
    while len(lst) > MAX_LENGTH:
        lst.pop()
    print(lst)












if __name__ == "__main__":
    
    add_many_numbers()
    double_list()
    canvas = SimpleCanvas(400, 400)
    canvas.create_rectangle(50, 50, 150, 150, 'blue')
    canvas.root.mainloop()
    add_three_copies()
    first_element_list()
    last_element_list()
    show_list()
    show_generated_list()




