
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

def add_fruit(L):
    fruit = get_string("Please enter the fruit you would like to add: -> ")
    number = get_integer("How many {}'s are you adding? -> ".format(fruit))
    temp_list = [number, fruit]
    L.append(temp_list)
    print("*" * 50)
    print("You have added {} {}'s to the list".format(number, fruit))

def main():
    print("Main function")
    base = [
        [0, "Bananas"],
        [0, "Oranges"],
        [0, "Apples"],
        [0, "Mangoes"]
    ]
    base = []
    my_menu = [
        ("A:", "Review"),
        ("B:", "Add Fruit"),
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
        elif choice =="Q":
            print("*" * 50)
            print("Thank you!")
            run = False
        else:
            print("Invalid entry ")


if __name__=="__main__":
    main()

