
def get_integer(m):
    my_integer = int(input(m))
    return my_integer

def get_string(m):
    my_string = input(m)
    return my_string

base = [
        [0, "Bananas"],
        [0, "Oranges"],
        [0, "Apples"],
        [0, "Mangoes"]
    ]

def review(L):
    print("*" * 50)
    print("Review Fruit:")
    for i in range(0, len(L)):
        output = "You have {} {}".format(L[i][0], L[i][1])
        print(output)


def single_loop_print(L):
    for i in range(0, len(L)):
        output = "{:10} --- {:10} --- {:<10}".format(i, L[i][0], L[i][1])
        print(output)

fruit_list = []

def add_fruit():







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
    my_index = get_integer("Please choose a fruit to update: -> ")
    new_amount = get_integer("Please enter the number of this fruit you are adding to the bowl: -> ")
    old_amount = L[my_index][0]
    my_sum = L[my_index][0] + new_amount
    final_amount = my_sum
    output = ("The number {} has been changed to {}".format(old_amount, final_amount))
    print(output)


def update_fruit_menu(L):
    my_menu = [
        ("A:", "Add fruit"),
        ("B:", "Subtract fruit"),
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
            update_fruit_add(base)
            print("*" * 50)
        elif choice == "B":
            print("Update Fruit - Subtract fruit:")
            print("*" * 50)
            print("*" * 50)
        elif choice =="C":
            review(base)
            print("*" * 50)
        elif choice == "Q":
            print("*" * 50)
            main()
        else:
            print("Invalid entry ")


#review(base)
update_fruit_menu(base)