feet_inches = input("Enter the feet and inches:")

def convert():
    try:
        parts = feet_inches.split(" ")
        feet = float(parts[0])
        inches = float(parts[1])

        meters = feet * 0.3048 + inches * 0.245
        return meters
    except TypeError:
        print("please enter in numbers")

result = convert()
if result > 1:
    print("the kid can use the slide:)")
else:
    print("The kid cannot use the slide:(")