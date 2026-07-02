try:
    age = int(input("ENTER YOUR AGE: "))
    if(age < 18):
        raise ValueError
    else:
        print("THE AGE IS VALID!!!!!")
        if age % 2 == 0:
            print("Also, your age is even.")
        else:
            print("Also, your age is odd.")

except ValueError:
    print("THE AGE IS INVALID!!!!!")