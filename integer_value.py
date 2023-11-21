#Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer.

def int_value():
    try:
        result = int(input("Enter a vlaue"))
        return result

    except ValueError:
        print("Enter correct integer value")


int_value()
