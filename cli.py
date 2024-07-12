#todos = []   #we are assigning list into a variable called todos (we must use [] :square bracket for set function , it is mutable
 # and we are giving this list to store the data which we will add in the match case function in while loop
# from function import get_todos, write_todos
import function
import time

now = time.strftime("  %d - %b -  %Y, %H %M %S")
print("Now time is: ",now)

" " "helo" " "
while True:
    user_action = input("type add, show, edit or exit:")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:] + '\n'
        todos = function.get_todos()

        todos.append(todo)

        function.write_todos(todos)


    elif user_action.startswith("show"):
        todos = function.get_todos()
        for index,  item in enumerate( todos):
            print( f"{index + 1}:){item.capitalize()}")
            #print(row)
# item = item.strip('\n')

    elif user_action.startswith("edit"):
        try:
              number = int(user_action [5:])
              print(number)
              number = number-1

              new_todo = input("enter the new todo")
              todos[number] = new_todo + '\n'

              function.write_todos(todos)

              function.get_todos()
              print("here is your edited content of your file:", todos)
                    #print("here is your edied file:", todos())

        except ValueError:
                print("Your command is no valid!!")
                continue

    elif user_action.startswith("delete"):
        try:
            function.get_todos()

            print("here is your prevailing content of your file:", todos)
            number = int(user_action [7:])
            todos.pop(number - 1)
            function.get_todos()
            function.write_todos(todos)
            print("here is your content after deletion :", todos)
            # for index, item  in enumerate (todos):
            #     print(f"Here is your edited todos list: {item}")
        except IndexError:
            print("There is no such value !!!")
            continue


    elif user_action.startswith('exit'):
        break

    else:
        print("The command you entered is  not valid")
    # if '_' in user_action:
    #     print("Hey you idiot, entered an unknown command!!!! run the program again")

print("Bye! Bye!")
