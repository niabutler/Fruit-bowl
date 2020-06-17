from validations import get_validated_integer
import math

def get_integer(m):
    my_integer = int(input(m))
    return my_integer

def get_string(m):
    my_string = input(m)
    return my_string


def review(L):
    for i in range(0, len(L)):
        output = "You have {} {}'s".format(L[i][0], L[i][1])
        print(output)

def single_loop_print(L):
    for i in range(0, len(L)):
        output = "{}: {}'s -- {}".format(i, L[i][1], L[i][0])
        print(output)

def add_fruit(L):
    fruit = get_string("Please enter the fruit you would like to add: -> ")
    number = get_validated_integer("How many {}'s are you adding? -> ".format(fruit), 0, math.inf)
    temp_list = [number, fruit]
    L.append(temp_list)
    print("*" * 50)
    print("You have added {} {}'s to the list".format(number, fruit))
    print("Please enter a number.")

def update_fruit_add(L):
    print("Update fruit")
    single_loop_print(L)
    # get index number taken from the printed menu before
    my_index = get_validated_integer("Please choose the number of the fruit to update: -> ", 0, len(L))
    # get amount to add onto the orginal number of fruit in the bowl
    new_amount = get_validated_integer("Please enter the number of this fruit you are adding to the bowl: -> ", 0, float('inf'))
    old_amount = L[my_index][0]
    my_sum = L[my_index][0] + new_amount
    L[my_index][0] = my_sum
    final_amount = my_sum
    output = ("The number of {} has been changed from {} to {}".format(L[my_index][1], old_amount, final_amount))
    print(output)

def update_fruit_subtract(L):
    print("Update fruit")
    single_loop_print(L)
    # get index number taken from the printed menu before
    my_index = get_validated_integer("Please choose the number of the fruit to update: -> ", 0, len(L))
    old_amount = L[my_index][0]
    # get amount to subtract from the orginal number of fruit in the bowl
    new_amount = get_validated_integer("Please enter the number of this fruit you are subtracting from the bowl: -> ", 1, old_amount)
    my_sum = L[my_index][0] - new_amount
    if new_amount >= old_amount:
        my_sum = 0
    else:
         L[my_index][0] = my_sum
    final_amount = my_sum
    output = ("The number of {} has been changed from {} to {}".format(L[my_index][1], old_amount, final_amount))
    print(output)



def update_fruit_menu(L):
    my_menu = [
        ("A:", "Add quantity of fruit"),
        ("B:", "Subtract quantity of fruit"),
        ("C:", "Review"),
        ("Q:", "Quit")
    ]
    run = True
    while run == True:
        # print main menu
        for i in range(0, len(my_menu)):
            print("{} {}".format(my_menu[i][0], my_menu[i][1]))
        choice = get_string("Please choose an option: -> ")
        if choice == "A":
            print("Update Fruit - Add fruit:")
            print("*" * 50)
            update_fruit_add(L)
            print("*" * 50)
        elif choice == "B":
            print("Update Fruit - Subtract fruit:")
            print("*" * 50)
            update_fruit_subtract(L)
            print("*" * 50)
        elif choice =="C":
            review(L)
            print("*" * 50)
        elif choice == "Q":
            print("*" * 50)
        else:
            print("Invalid entry ")

def main():
    print("Main function")
    base = [
        [0, "Bananas"],
        [0, "Oranges"],
        [0, "Apples"],
        [0, "Mangoes"]
    ]
    base = [[5, "Banana"]]
    my_menu = [
        ("A:", "Review Fruitbowl"),
        ("B:", "Add fruit to bowl"),
        ("C:", "Update Fruit Quantities"),
        ("Q:", "Quit")]
    run = True
    while run == True:
        # print main menu
        for i in range(0, len(my_menu)):
            print("{} {}".format(my_menu[i][0], my_menu[i][1]) )
        choice = get_string("Please choose an option: -> ")
        if choice =="A":
            print("Review Fruit:")
            print("*" * 50)
            review(base)
            print("*"*50)
        elif choice =="B":
            print("Add Fruit:")
            print("*" * 50)
            add_fruit(base)
            print("*" * 50)
        elif choice =="C":
            if len(base) == 0:
                print("There is nothing in your fruitbowl to update. Please add items to update.")
                print("*" * 50)
            else:
                print("Update Fruit Quantities:")
                print("*" * 50)
                update_fruit_menu(base)
                print("*" * 50)
        elif choice =="Q":
            print("*" * 50)
            print("Thank you!")
            run = False
        else:
            print("Invalid entry ")


if __name__=="__main__":
    main()


