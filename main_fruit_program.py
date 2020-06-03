
def get_integer(m):
    my_integer = int(input(m))
    return my_integer

def get_string(m):
    my_string = input(m)
    return my_string


def review(L):
    for i in range(0, len(L)):
        output = "You have {} {}".format(L[i][0], L[i][1])
        print(output)

def main():
    print("Main function")
    base = [
        [0, "Bananas"],
        [0, "Oranges"],
        [0, "Apples"],
        [0, "Mangoes"]
    ]
    my_menu = [
        ("A:", "Review"),
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
        elif choice =="Q":
            print("*" * 50)
            print("Thank you!")
            run = False
        else:
            print("Invalid entry ")


if __name__=="__main__":
    main()

