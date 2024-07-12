# date = input("Enter the date :")
# mood = ("How do you rate your mood from the scale of 1 to 10 ?:")
# journal = ("Let your thoughts flow : \n  ")
#
# with open(f ". . / journal/ {date}  .txt",  'w') as file:
# file.write(mood)
# file.write(journal)
#
date = input("Enter the date: ")
mood = input("How do you rate your mood from the scale of 1 to 10?: ")
thoughts = input("Let your thoughts flow:\n")

# Corrected file path and writing to file
with open(f". . venv/lib/scripts {date}.txt", 'w') as file:
    file.write(thoughts)
    file.write(mood)
