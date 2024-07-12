todos = []   # We are assigning a list to a variable called todos. We must use [] (square brackets) for a list, which is mutable. This list is used to store the data we will add in the match case function in the while loop.

while True:
    user_action = input("type add, show, edit or exit:")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:] + '\n'
        with open('vic.txt', 'r') as file:
            todos = file.readlines()
            todos.append(todo)

        with open('vic.txt', 'w') as file:
            file.writelines(todos)

    elif user_action.startswith("show"):
        with open('vic.txt', 'r') as file:
            todos = file.readlines()
        for index, item in enumerate(todos):
            print(f"{index + 1}: {item.capitalize().strip()}")

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            print(number)
            number = number - 1

            new_todo = input("Enter the new todo: ").strip()
            todos[number] = new_todo + '\n'

            with open('vic.txt', 'w') as file:
                file.writelines(todos)

            with open('vic.txt', 'r') as file:
                todos = file.readlines()
                print("Here is your edited content of your file:", todos)

        except ValueError:
            print("Your command is not valid!!")
            user_action = input("type add, show, edit or exit:").strip()

    elif user_action.startswith("complete"):
        with open('vic.txt', 'r') as file:
            todos = file.readlines()
            print("Here is your prevailing content of your file:", todos)
        number = int(user_action[9:])

        todos.pop(number - 1)
        with open('vic.txt', 'w') as file:
            file.writelines(todos)
        print(todos)

    elif user_action.startswith('exit'):
        break

    else:
        print("The command you entered is not valid")
    # if '_' in user_action:
    #     print("Hey you idiot, entered an unknown command!!!! run the program again")

print("Bye! Bye!")
