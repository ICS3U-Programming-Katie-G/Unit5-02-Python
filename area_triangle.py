#!/usr/bin/env python3
# Created by: Katie G
# Created on: December 15th, 2022
# This program will get the user's base and height
# of their triangle in main, ensure the user's input is
# valid, then it will pass the base and height to the calc_area function
# as arguments. the calc_area function will calculate the area and display it
# back to the user.


# this function will calculate the area of the triangle using
# the base and height of the triangle, which was obtained
# in pain and passed to this function.
def calc_area(base, height):
    # calculating the area of the triangle with user values.
    area = (base * height) / 2

    # display the results of the calculation back to the user.
    print(
        "The area of the triangle with base {} and height {} is {} cm^2".format(
            base, height, area
        )
    )


# this function will get the user base and height, and then
# check to make sure the user input is error-free.
def main():
    # getting the user's base and height.
    user_base = input("Please enter your triangle's base in centimeters: ")
    user_height = input("Please enter your triangle's height in centimeters: ")

    # try...catch to make sure the user input is valid.
    try:
        user_base_int = float(user_base)
        if user_base_int >= 0:
            try:
                user_height_int = float(user_height)
                if user_height_int >= 0:
                    calc_area(user_base_int, user_height_int)
                else:
                    print("Please enter a valid, positive integer!")
            except Exception:
                print("Please enter a valid integer!")
        else:
            print("Please enter a valid, positive integer!")
    except Exception:
        print("Please enter a valid integer!")


if __name__ == "__main__":
    main()
