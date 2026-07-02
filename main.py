try:
    number = int(input("PLEASE ENTER A NUMBER: "))
    print("YOU HAVE ENTERED: ", number)

except ValueError as x:
    print("EXCEPTION: ", x)
    