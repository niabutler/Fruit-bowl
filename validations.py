def get_validated_integer(m, min, max):
    while True:
        try:
            number = int(input(m))
        except ValueError:
            print("This is not a valid entry.")
            continue
        if number < min:
            print("Your entry is too small")
            continue
        elif number > max:
            print("Your entry is too big")
        else:
            return number








if __name__ =="__main__":
    get_validated_integer("Please enter your number: ->", 0, 5)


