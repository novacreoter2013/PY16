valid = False
while not valid:
    try:
        num = int(input("PLEASE ENTER A NUMBER: "))
        while num%2 == 0:
            print("BYE BYE")
            valid = True
    except ValueError:
        print("WRONG INPUT!!!!")
