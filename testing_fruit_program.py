
def get_integer(m):
    my_integer = int(input(m))
    return my_integer

def get_string(m):
    my_string = input(m)
    return my_string



def review(L):
    print("*" * 50)
    print("Review Fruit:")
    for i in range(0, len(L)):
        output = "You have {} {}".format(L[i][0], L[i][1])
        print(output)


def single_loop_print(L):
    for i in range(0, len(L)):
        output = "{}: {}'s -- {}".format(i, L[i][1], L[i][0])
        print(output)

def adding(a,b):
    my_sum = a+b
    my_string = "{} + {} = {}".format(a,b,my_sum)
    print(my_string)


def update_name(L):
    print("Update a name.")
    single_loop_print(L)
    my_index = get_integer("Please choose an index number to update: -> ")
    new_number = get_string("Please enter a new name: -> ")
    old_name = L[my_index][0]
    L[my_index][0] = new_number
    output = ("The name {} has been changed to {}".format(old_name, new_number))
    print(output)


def update_fruit_add(L):
    print("Update fruit")
    single_loop_print(L)
    my_index = get_integer("Please choose the number of the fruit to update: -> ")
    new_amount = get_integer("Please enter the number of this fruit you are adding to the bowl: -> ")
    old_amount = L[my_index][0]
    my_sum = L[my_index][0] + new_amount
    L[my_index][0] = my_sum
    final_amount = my_sum
    output = ("The number of {} has been changed from {} to {}".format(L[my_index][1], old_amount, final_amount))
    print(output)

def update_fruit_subtract(L):
    print("Update fruit")
    single_loop_print(L)
    my_index = get_integer("Please choose the number of the fruit to update: -> ")
    new_amount = get_integer("Please enter the number of this fruit you are subtracting from the bowl: -> ")
    old_amount = L[my_index][0]
    my_sum = L[my_index][0] - new_amount
    L[my_index][0] = my_sum
    final_amount = my_sum
    output = ("The number of {} has been changed from {} to {}".format(L[my_index][1], old_amount, final_amount))
    print(output)


def update_fruit_menu():
    my_menu = [
        ("A:", "Add fruit"),
        ("B:", "Subtract fruit"),
        ("C:", "Review"),
        ("Q:", "Quit")
    ]

    base = [
        [0, "Bananas"],
        [0, "Oranges"],
        [0, "Apples"],
        [0, "Mangoes"]
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
            update_fruit_add(base)
            print("*" * 50)
        elif choice == "B":
            print("Update Fruit - Subtract fruit:")
            print("*" * 50)
            update_fruit_subtract(base)
            print("*" * 50)
        elif choice =="C":
            review(base)
            print("*" * 50)
        elif choice == "Q":
            print("*" * 50)
        else:
            print("Invalid entry ")



def add_fruit():
    L = []
    fruit = get_string("Please enter the fruit you would like to add: -> ")
    number = get_integer("Please enter the amount of this fruit you have: -> ")
    temp_list = [fruit, number]
    L.append(temp_list)
    print(L)

#review(base)
update_fruit_menu()
#add_fruit()