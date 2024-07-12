try:
    width = float(input("Enter rectangle width: "))
    length = float(input("Enter rectangle length: "))
    if width == length:
        exit("That looks like a square****")

    area = width*length
    print('The area of the rectangle is :', area)
except ValueError:
    print("Please enter a number!!")
